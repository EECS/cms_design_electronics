import re, pdb

HTML_GEN_CONVERTER_BUTTON = "generateConverterButton"
HTML_GEN_COMPONENTS_ID="generateRecommendedComponents"
HTML_GEN_ANALYSIS_ID="generateConverterAnalysis"
HTML_GEN_COMPONENTS_TAG="design_parameter_"
HTML_GEN_ANALYSIS_TAG="sel_component_"
HTML_REC_COMPONENTS_TAG="rec_component_"

DCDC_CURRENT_TYPE = (
    ("ccm", "Continuous Conduction Mode"),
    ("dcm", "Discontinuous Conduction Mode"),
)

UNITS = (
    ("kHz", "kHz"),
    ("microHenries", "microHenries"),
    ("microFarads", "microFarads"),
    ("Volts", "V"),
    ("Amps", "A"),
    #Duty Ratio Units
    ("Duty Cycle", None),
    ("%", "%"),
    ("Ohms", "Ohms"),
)

#ADD to unit conversions when units added to UNITS
UNIT_CONVERSIONS ={
    #Switching Frequency
    UNITS[0][1]: 1000,
    #Inductance
    UNITS[1][1]: 1e-6,
    #Capacitance
    UNITS[2][1]: 1e-6,
    #Volts
    UNITS[3][1]: 1,
    #Amps
    UNITS[4][1]: 1,
    #Duty Ratio
    UNITS[5][1]: 1,
    #Percent
    UNITS[6][1]: 1e2,
    #Ohms
    UNITS[7][1]: 1
}

def substitute_expression(expression, values):
    '''
    params: expression (string) - An expression that needs 
    values substituted.
    values (dictionary) - A dictionary with key of the component (e.g. R1)
    and the value corresponding with the wanted quantity to substitute in the
    expression string.
    '''
    function = expression

    for k, v in values.items():
        function = re.sub(r"\b{}\b".format(k), "({})".format(str(v)), function)
    
    return function

def calculate_duty_cycle(duty_cycle_expression):
    '''
    params: input_output_transfer (Sympy expression) - A
    sympy variable in the s-domain to be used to calculate the duty cycle.
    d_idx (int) - Index of solved duty_cycle equation to return (important for
    sqrt operations.)
    '''

    return duty_cycle_expression

def generate_transfer_data(transfer_function, bode_x_range):
    '''
    params: transfer_function (string) s-domain transfer function consisting of values to
    be used for evaluation.
    bode_x_range: (list) Hz values spaced by logarithmic steps to be used to generate
    phase and magnitude data.
    '''
    denom_start = transfer_function.find("/")
    mags = []
    phases = []

    #Create numerator and denominator strings of the transfer function.
    if denom_start != -1:
        numerator = transfer_function[:denom_start]
        denominator = transfer_function[denom_start+1:]
    else:
        numerator = transfer_function
        denominator = str(1)

    #Create magnitude and phase arrays for transfer function, replacing s with 
    #the angular frequency representation.
    for f in bode_x_range:
        complex_replace = str(2j*cmath.pi*f)
        complex_replace = "({})".format(complex_replace)

        if denom_start != -1:
            num = numerator.replace("s", complex_replace)
            c_num = complex(eval(num))
            denom = denominator.replace("s", complex_replace)
            c_denom = complex(eval(denom))
            c_denom_conj = c_denom.conjugate()
            c_transfer = (c_num/c_denom)*(c_denom_conj/c_denom_conj)
        else:
            c_transfer = complex(transfer_function.replace("s", complex_replace))

        mags.append(20*math.log10(abs(c_transfer)))
        phases.append(cmath.phase(c_transfer)*180/cmath.pi)
    
    return mags, phases

def clean_dcdc_form(tag, value, param):
    '''
    params: tag (str) HTML tag appended to front of component/param for HTML
    ID purposes.
    param: (str) Parameter or component to be cleaned.
    value: (float) Value of parameter or component to be cleaned.
    returns (int) a cleaned value of the selected parameter/component, False if there
    is an error with cleaning the parameter/component.
    '''

    param = param[len(tag):]
    #Switching frequency parameter.
    if param == "Fs":
        if value <= 0:
            return False
        return value*UNIT_CONVERSIONS["kHz"]
    elif param == "VD1":
        if value < 0:
            return False
        return value*UNIT_CONVERSIONS["V"]
    elif param == "RipIo":
        if value <= 0:
            return False
        return value*UNIT_CONVERSIONS["A"]
    elif param == "RipVo":
        if value <= 0:
            return False
        return value*UNIT_CONVERSIONS["V"]
    
    return value

def calculate_dcdc_components(params, recommended_components):
    '''
    params: params (dict) dictionary of key param (Vo, Vin, etc.) and
    value of key in correct units.
    recommended_components (model_cluster) cluster of recommended components
    to generate values for.
    '''
    components = {}
    unit_dict = dict(UNITS)

    for component in recommended_components.values():
        expr = substitute_expression(component["equation"], params)
        expr = eval(expr)

        #Convert expression to correct units.
        expr /= UNIT_CONVERSIONS[unit_dict[component["units"]]]

        components.update({"{}{}"\
                    .format(HTML_REC_COMPONENTS_TAG,component["abbreviation"]): 
                            round(expr, 2)})
    
    return components

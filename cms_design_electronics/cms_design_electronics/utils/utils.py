import re, math, cmath
import pdb

HTML_GEN_CONVERTER_BUTTON = "generateConverterButton"
HTML_GEN_OPENLOOP_BUTTON = "generateOpenLoopButton"

HTML_GEN_COMPONENTS_ID="generateRecommendedComponents"
HTML_GEN_ANALYSIS_ID="generateConverterAnalysis"
HTML_GEN_OPENLOOP_ID="generateOpenLoopTransfers"
HTML_OPEN_LOOP_ID="open_plot_"

HTML_GEN_COMPONENTS_TAG="design_parameter_"
HTML_GEN_ANALYSIS_TAG="sel_component_"
HTML_REC_COMPONENTS_TAG="rec_component_"
HTML_DESIGN_EQUATIONS_TAG="design_equation_"

MODEL_DUTY_RATIO = "Duty Ratio"
MODEL_RIPPLE_VOLTAGE = "Ideal Output Ripple Voltage"
MODEL_OUTPUT_VOLTAGE ="Vo"
MODEL_EQUATION_DUTY_RATIO = "D"

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
    UNITS[6][1]: 1e-2,
    #Ohms
    UNITS[7][1]: 1
}

assert len(UNITS) == len(UNIT_CONVERSIONS)

def fill_zeros(start_freq=1, end_freq=100, num_points=5000):
    '''
    Generates a list of data points between start_freq and end_freq
    with all 0.
    params: start_freq (int) - Starting frequency in Hz
    end_freq (int) - Ending frequency in kHz
    num_points (int) - Number of points in returned list.j
    returns:
    log_x_range (list) list of points between start and end freq as 0.
    '''

    x_range = [0 for i in range(num_points)]

    return x_range

def log_step_size(start_freq=1, end_freq=100, num_points=5000):
    '''
    Generates a list of data points between start_freq and end_freq
    using a logarithmic step size.
    params: start_freq (int) - Starting frequency in Hz
    end_freq (int) - Ending frequency in kHz
    num_points (int) - Number of points in returned list.j
    returns:
    log_x_range (list) list of points between start and end freq.
    '''

    log_step_size = ((math.log10(end_freq*1000)-math.log10(start_freq))/num_points)
    log_x_range = [10**((i+1)*log_step_size) for i in range(num_points)]

    return log_x_range

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
    elif param == "Io":
        return value*UNIT_CONVERSIONS["A"]
    elif param == "Vin" or param=="Vo":
        return value*UNIT_CONVERSIONS["V"]
    elif param == "C1":
        if value < 0:
            return False
        return value*UNIT_CONVERSIONS["microFarads"]
    elif param == "L1":
        if value < 0:
            return False
        return value*UNIT_CONVERSIONS["microHenries"]
    elif param == "RC1" or param=="RL1" or param=="RQ1":
        if value < 0:
            return False
        return value*UNIT_CONVERSIONS["Ohms"]

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

def generate_dcdc_analysis(params_components, design_equations):
    '''
    params_components: params (dict) dictionary of key param/component
    (Vo, Vin, etc.) and value of key in correct units.
    design_equations (model_cluster) cluster of design equations
    to generate results for.
    '''
    results = {}
    unit_dict = dict(UNITS)

    for equation in design_equations.values():
        expr = substitute_expression(equation["equation"], params_components)
        expr = eval(expr)

        #Convert expression to correct units.
        expr /= UNIT_CONVERSIONS[unit_dict[equation["units"]]]

        if equation["description"] == MODEL_DUTY_RATIO:
            if expr >=1 or expr <= 0:
                expr = False
        elif equation["description"] == MODEL_RIPPLE_VOLTAGE:
            if expr >= params_components[MODEL_OUTPUT_VOLTAGE]:
                expr = False
        
        #Analysis obtained successful results.
        if expr:
            results.update({"{}{}"\
                    .format(HTML_DESIGN_EQUATIONS_TAG,equation["description"]): 
                            round(expr, 3)})
        #Error with analysis
        else:
            results.update({"{}{}"\
                    .format(HTML_DESIGN_EQUATIONS_TAG,equation["description"]): 
                            expr})
            break
    
    return results


def generate_open_loop(params_components, design_equations, bode_x_range):
    '''
    Generates magnitude and phase data for all open loop transfer functions.
    params: 
    params_components: params (dict) dictionary of key param/component
    (Vo, Vin, etc.) and value of key in correct units.
    design_equations (model_cluster) cluster of open loop design equations
    to generate results for.
    bode_x_range (list) list of frequencies to generate magnitude and phase
    data for.
    '''
    results = {}

    for equation in design_equations.values():
        expr = substitute_expression(equation["equation"], params_components)
        mags, phases = generate_transfer_data(expr, bode_x_range)
        results[equation["description"]] = [mags, phases]
    
    return results
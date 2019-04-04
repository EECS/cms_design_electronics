from django import forms
from django.db import models
from django.http import JsonResponse

from modelcluster.fields import ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from ..streams import blocks
from ..snippets import snippets
from ..utils import utils

import pdb

#Ajax support for webpage
import json
from django.http import HttpResponse

class DcdcPage(Page):
    """DC/DC Converter page model."""

    template = "dcdc/dcdc_page.html"

    design_name = models.CharField(
        max_length=75,
        blank=False, 
        null=True,
        verbose_name="DC/DC Converter Name",
    )

    design_description = StreamField([
        ("description", blocks.RichtextBlock()),
    ], null=True, blank=False, verbose_name="Design Description")
    
    design_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Circuit Image",
    )

    dcdc_type = models.CharField(
        max_length=75, 
        choices=utils.DCDC_CURRENT_TYPE, 
        blank=False, 
        null=True,
        verbose_name="DC/DC Current Type",
    )

    design_params = ParentalManyToManyField(
                            snippets.DCDCDesignParam,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Design Parameters",
    )

    recommended_components = ParentalManyToManyField(
                            snippets.DCDCRecComps,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Recommended Components",
    )

    selected_components = ParentalManyToManyField(
                            snippets.DCDCSelComps,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Selected Components",
    )

    design_equations = ParentalManyToManyField(
                            snippets.DCDCDesignEquations,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Design Equations",
    )

    open_loop_equations = ParentalManyToManyField(
                            snippets.DCDCOpenLoopEquations,
                            blank=False, #Required entry
                            related_name="+",
                            verbose_name="Open Loop Transfer Functions",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("design_name"),
                StreamFieldPanel("design_description"),
                ImageChooserPanel("design_image"),
                FieldPanel("dcdc_type"),
            ],
            heading="DC/DC Converter Description",
        ),
        MultiFieldPanel(
            [
                FieldPanel("design_params", widget=forms.CheckboxSelectMultiple),
                FieldPanel("recommended_components", widget=forms.CheckboxSelectMultiple),
                FieldPanel("selected_components", widget=forms.CheckboxSelectMultiple),
            ],
            heading="DC/DC Converter Design Parameters and Components",
        ),
        MultiFieldPanel(
            [
                FieldPanel("design_equations", widget=forms.CheckboxSelectMultiple),
                FieldPanel("open_loop_equations", widget=forms.CheckboxSelectMultiple),
            ],
            heading="DC/DC Converter Open Loop Design Equations",
        ),
    ]

    gen_components_context = "generated_components"
    rec_components_context = "recommended_components"
    gen_analysis_context = "generated_analysis"
    csrftoken_context = "csrfmiddlewaretoken"

    class Meta:

        verbose_name = "DC/DC Converter Page"
        verbose_name_plural = "DC/DC Converter Pages"

    def __str__(self):
        return self.design_name
    
    def get_context(self, request):
        context = super(DcdcPage, self).get_context(request)

        #Update context if an ajax request is submitted with
        #design data.
        if request.is_ajax():

            #Generate recommended components
            if utils.HTML_GEN_COMPONENTS_ID in request.POST:
                #Filter to get only parameters for analysis.
                #form keys are in the form of design_parameter_PARAM: value
                #this trims it to PARAM: cleaned_value
                cleaned_params = {key[len(utils.HTML_GEN_COMPONENTS_TAG):]:utils.clean_dcdc_form(utils.HTML_GEN_COMPONENTS_TAG, float(value), key) \
                    for (key, value) in request.POST.items() if key != self.csrftoken_context and key != utils.HTML_GEN_COMPONENTS_ID}

                '''Error with form submission values.'''
                if False in cleaned_params.values():
                    '''Build list of values with an error'''
                    error_dict = {}
                    for key, value in cleaned_params.items():
                        if not value:
                            error_dict.update({"{}{}".format(utils.HTML_GEN_COMPONENTS_TAG, key):"Enter a valid value for this parameter."})

                    context.update({self.rec_components_context:error_dict})
                    context.update({self.gen_components_context: False})
                else:
                    components = utils.calculate_dcdc_components(cleaned_params, self.recommended_components)
                
                    context.update({self.rec_components_context:components})
                    context.update({self.gen_components_context: True})

        return context
    
    def serve(self, request):

        if request.is_ajax():
            context = self.get_context(request)

            if utils.HTML_GEN_COMPONENTS_ID in request.POST:
                response = JsonResponse(context[self.rec_components_context])

                #If components could be generated
                if context[self.gen_components_context]:
                    return response
                
                #Error with generating components.
                response.status_code = 403
                return response

            #Generate converter analysis
            elif utils.HTML_GEN_ANALYSIS_ID in request.POST:

                #Ensure that design parameters have been input
                #which occurs when components have been generated
                if (generated_components in context and 
                    context[generated_components]):
                    pass
                #Design parameters must be submitted prior to conducting
                #converter analysis.
                else:
                    pass


        else:
            return super(DcdcPage, self).serve(request)
from django import forms
from diagnosise.models import Diagnosis


class TextInputForm(forms.Form):
    '''Form for user's health complaints'''
    symptoms = forms.CharField(max_length=250, empty_value=False, label=False,
                               widget=forms.Textarea(attrs={'class': 'form-control'}))
    

# class DiagnosiseSaveForm(forms.Form):
#     '''Form to save data'''
#     symptoms = forms.CharField(max_length=250, empty_value=False,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))

#     disease_category = forms.CharField(max_length=150, empty_value=False,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
#     description = forms.Fi
    


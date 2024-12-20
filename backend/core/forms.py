from django import forms

from .models import User, Appointment

from core.models import SPECIALIZATIONS


class AppointmentForm(forms.ModelForm):

    first_name = forms.CharField(label='Имя', disabled=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    last_name = forms.CharField(label='Фамилия', disabled=True, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.CharField(label='Email', disabled=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    phone = forms.CharField(label='Номер телефона', required=False, empty_value=True,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}),
                            disabled=False,)
    
    # specialization = forms.CharField(label='Специализация врача', required=False,
    #                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    specialization = forms.ChoiceField(label='Специализация врача',
                                       choices=SPECIALIZATIONS,
                                       widget=forms.Select(attrs={'class': 'form-select'}),)
    
    comment = forms.CharField(label='Комментарий', required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))

    

    class Meta:
        model = Appointment
        fields = ('first_name', 'last_name', 'email', 'phone', 'specialization', 'comment')
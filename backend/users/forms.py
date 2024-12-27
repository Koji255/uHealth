import re

from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError

from users.models import User



class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField(label='Username',
                               max_length=50,
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'text',
                                   'placeholder': 'Username',
                                   }))
    
    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.EmailInput(attrs={
                                   'class': 'form-control',
                                   'type': 'email',
                                   'placeholder': 'example@yandex.ru',
                                   }))
    
    phone = forms.CharField(label='Phone',
                            help_text='(optional)',
                            required=False,
                            max_length=15,
                            validators=[RegexValidator(regex=r'^(\+7|8)?\d{10}$', message="Enter a valid phone number.")],
                            widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'tel',
                                   'placeholder': '8-123-456-78-90',
                                   'pattern': '[0-9\ ]+',
                                   }))
    
    first_name = forms.CharField(label='First Name',
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'text',
                                   'placeholder': 'First Name',
                                   }))
    
    last_name = forms.CharField(label=False,
                                help_text='(optional)',
                                required=False,
                                widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'text',
                                   'placeholder': 'Last Name',
                                   }))
    
    password1 = forms.CharField(label='Password', required=True,
        error_messages={
        'required': 'Password is required.',
        'min_length': 'Password must be at least 8 characters long.',
        'max_length': 'Password cannot exceed 128 characters.',
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Password',
        })
    )

    password2 = forms.CharField(label=False, required=True,
        error_messages={
        'required': 'Confirm your password.'
        },

        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Confirm Password'
        }),
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')
    

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        if phone and not re.match(r'^[+]?[\d\s-]+$', phone):
            raise ValidationError('Invalid phone number format.')
        
        return phone



class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(label='Username',
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    password = forms.CharField(label='Password',
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "password")

    # Username Validation
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise ValidationError('Username cannot contain spaces.')
        return username

    # Password Validation
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match.')
        
        return cleaned_data



class UserProfileForm(forms.ModelForm):

    username = forms.CharField(label='Username', required=False, initial='',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    first_name = forms.CharField(label='First Name', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    last_name = forms.CharField(label='Last Name', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.CharField(label='Email', disabled=True, 
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
    
    phone = forms.CharField(label='Phone Number', required=False,
                            validators=[RegexValidator(regex=r'^(\+7|8)?\d{10}$', message='Enter a valid phone number.')],
                            widget=forms.TextInput(attrs={
                                'class': 'form-control', 
                                # 'type': 'tel',
                                'placeholder': '81234567890',
                                }))
    
    birthday = forms.DateField(label='Birthday', required=False, localize='Ru',
                               widget=forms.DateInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'DD|MM|YYYY'
                                   }))


    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'phone')
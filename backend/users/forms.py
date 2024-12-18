import re

from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError

from users.models import User



class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField(label='Имя пользователя',
                               max_length=50,
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'text',
                                   'placeholder': 'Логин',
                                   }))
    
    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.EmailInput(attrs={
                                   'class': 'form-control',
                                   'type': 'email',
                                   'placeholder': 'example@yandex.ru',
                                   }))
    
    phone = forms.CharField(label='Номер телефона',
                            help_text='(необязательно)',
                            required=False,
                            max_length=15,
                            validators=[RegexValidator(regex=r'^(\+7|8)?\d{10}$', message="Введите правильный номер телефона.")],
                            widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'tel',
                                   'placeholder': '8-123-456-78-90',
                                   'pattern': '[0-9\ ]+',
                                   }))
    
    first_name = forms.CharField(label='Персональные данные',
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'text',
                                   'placeholder': 'Имя',
                                   }))
    
    last_name = forms.CharField(label=False,
                                help_text='(необязательно)',
                                required=False,
                                widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'type': 'text',
                                   'placeholder': 'Фамилия',
                                   }))
    
    password1 = forms.CharField(label='Пароль', required=True,
        error_messages={
        'required': 'Пароль обязателен.',
        'min_length': 'Пароль должен содержать не менее 8 символов.',
        'max_length': 'Пароль не должен превышать 128 символов.'
        },

        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Пароль',
        })
    )

    password2 = forms.CharField(label=False, required=True,
        error_messages={
        'required': 'Подтвердите пароль.'
        },

        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Подтверждение пароля'
        }),
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')
    

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        
        if phone and not re.match(r'^[+]?[\d\s-]+$', phone):
            raise ValidationError('Некорректный формат номера телефона.')
        
        return phone



class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(label='Имя пользователя',
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    password = forms.CharField(label='Пароль',
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "password")

    # Username Validation
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise ValidationError('Имя пользователя не должно содержать пробелов.')
        return username

    # Password Validation
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают.')
        
        return cleaned_data



class UserProfileForm(forms.ModelForm):

    username = forms.CharField(label='Имя пользователя', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    first_name = forms.CharField(label='Имя', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    last_name = forms.CharField(label='Фамилия', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.CharField(label='Email', disabled=True, 
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
    
    phone = forms.CharField(label='Номер телефона', required=False,
                            validators=[RegexValidator(regex=r'^(\+7|8)?\d{10}$', message="Введите правильный номер телефона.")],
                            widget=forms.TextInput(attrs={
                                'class': 'form-control', 
                                # 'type': 'tel',
                                'placeholder': '81234567890',
                                }))
    
    birthday = forms.DateField(label='Дата рождения', required=False, localize='Ru',
                            #    validators=[RegexValidator(regex=r'^\d{4}-0([1-9]|1[0-2]){2}-(0[1-9]|1[0-31]|2[0-31]|3[031]){2}$', message="Введите правильную дату рождения.")],
                               widget=forms.DateInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'DD|MM|YY'
                                   }))
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'phone')
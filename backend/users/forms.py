from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from users.models import User



class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField(label='Имя пользователя',
                               max_length=50,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    phone = forms.CharField(label='Номер телефона',
                            help_text='необязательно',
                            required=False,
                            max_length=15,
                            validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Введите правильный номер телефона.")],
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    first_name = forms.CharField(label='Имя',
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    last_name = forms.CharField(label='Фамилия',
                                help_text='необязательно',
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    password1 = forms.CharField(label='Пароль',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    password2 = forms.CharField(label='Подтверждение пароля',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))



    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')



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



class UserProfileForm(forms.ModelForm):

    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.CharField(label='Email', disabled=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    phone = forms.CharField(label='Номер телефона', required=False, empty_value=True,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')
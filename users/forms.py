from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']






class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))


    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password1')
    #     confirm_password = cleaned_data.get('password2')
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError('Wrong password')
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])
    #     if commit:
    #         user.save()
    #     return user

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин' )
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}), disabled=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        labels = {
            'username': 'nickname',
            'email': 'e-mail',
        }



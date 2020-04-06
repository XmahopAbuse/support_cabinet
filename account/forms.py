from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'username',
        'placeholder':'Имя пользователя',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'id': 'password',
        'placeholder': 'Пароль',
    }))
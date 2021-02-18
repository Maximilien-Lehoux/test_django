from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='user name', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)


class FormLogin(forms.Form):
    user_name = forms.CharField(label='user name', max_length=100)
    password = forms.CharField(label='password', max_length=100)
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .views import Blog


class SubmitForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

# class LoginForm(AuthenticationForm):
#     class Meta:
#         widgets = {
#             'username' : TextInput(attrs = {'placeholder': 'Username'}),
#             'password'    : PasswordInput(attrs = {'placeholder': 'Password'}),
#         }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doneer, Donee
from django.contrib.auth import authenticate

class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if not user:
            raise forms.ValidationError("Invalid email or password")
        return cleaned_data

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    user_type = forms.ChoiceField(choices=[('doneer', 'Doneer'), ('donee', 'Donee')], required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # تعيين البريد الإلكتروني كاسم المستخدم
        if commit:
            user.save()
            user_type = self.cleaned_data['user_type']
            if user_type == 'doneer':
                Doneer.objects.create(
                    firstname=user.first_name,
                    lastname=user.last_name,
                    email=user.email,
                    password=self.cleaned_data['password1']
                )
            elif user_type == 'donee':
                Donee.objects.create(
                    firstname=user.first_name,
                    lastname=user.last_name,
                    email=user.email,
                    password=self.cleaned_data['password1']
                )
        return user

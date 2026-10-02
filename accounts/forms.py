from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'role',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )


class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('resume',)
        widgets = {
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'skills',
            'education',
            'experience',
            'bio',
            'resume',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone number',
                }
            ),
            'skills': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Python, Django, SQL, Git',
                }
            ),
            'education': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),
            'experience': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),
            'bio': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),
            'resume': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }

from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = (
            'title',
            'company_name',
            'description',
            'location',
            'salary',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. Python Backend Developer',
                }
            ),
            'company_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Company name',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'Job responsibilities and requirements',
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. Kolkata',
                }
            ),
            'salary': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Salary',
                    'min': 0,
                    'step': '0.01',
                }
            ),
        }

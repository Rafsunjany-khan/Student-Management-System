from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'course']

    # Field-level validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone) < 10 or len(phone) > 15:
            raise forms.ValidationError("Phone number must be between 10 and 15 digits.")
        return phone

    # Cross-field validation (example: phone or course should not be empty)
    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        course = cleaned_data.get('course')

        if not phone and not course:
            raise forms.ValidationError("Either phone or course should be provided.")

        return cleaned_data

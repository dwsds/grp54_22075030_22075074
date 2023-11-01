from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import OtherIllnesses

class IllnessForm(forms.Form):
    metabolic_stress = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[("Mental illness", "Mental illness"),
    ("Minor surgery", "Minor surgery"),
    ("Pregnancy/Lactation", "Pregnancy/Lactation"),
    ("Pregnancy with complications", "Pregnancy with complications"),
    ("Fever", "Fever"),
    ("Solid tumors/radiotherapy", "Solid tumors/radiotherapy"),
    ("Laproscopic surgeries", "Laproscopic surgeries"),
    ("Acute kidney disease", "Acute kidney disease"),
    ("Cardiac Disease", "Cardiac Disease"),
    ("Diabetes", "Diabetes"),
    ("Stroke", "Stroke"),
    ("Severe Pneumonia", "Severe Pneumonia"),
    ("Current cancer undergoing treatment", "Current cancer undergoing treatment"),
    ("Transplant surgeries", "Transplant surgeries"),
    ("Severe Sepsis", "Severe Sepsis"),
    ("Severe Acute Pancreatitis", "Severe Acute Pancreatitis"),
    ("None", "None")],
        required=False
    )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # You can use your custom user model here if you have one
        fields = ('username', 'email')  # Customize the fields you want in the form    
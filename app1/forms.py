from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import OtherIllnesses , DietChange,Physical,GastrSymptoms

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

class DietChangeForm(forms.Form):
    changes = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[("Sub-optimal solid diet","sub-optimal solid diet"),
    ("Taking liquids only","Taking liquids only"),
    ("Hypo caloric diet","Hypo caloric diet"),
    ("Virtually Nil/Starvation","Virtually Nil/Starvation"),
    ("No change","No change")],
        required=False
    )
   
class GastrSymptomsForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ("Nausea", "Nausea"),
            ("Vomiting/Diarrhea", "Vomiting/Diarrhea"),
            ("Severe Anorexia", "Severe Anorexia"),
            ("None", "None")
        ],
        required=False
    )

class PhysicalForm(forms.Form):
    phy_illness = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[("Edema","Edema"),
 ("Muscle Wasting","Muscle Wasting"),
 ("Fractures","Fractures"),
 ("Minor burns","Minor burns"),
 ("Major burns","Major burns"),
 ("Severe burns","Severe burns"),
 ("Head injury/ Multiple Trauma","Head injury/ Multiple Trauma")],
        required=False
    ) 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # You can use your custom user model here if you have one
        fields = ('username', 'email')  # Customize the fields you want in the form    

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
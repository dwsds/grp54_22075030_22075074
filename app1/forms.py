from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import OtherIllnesses , DietChange,Physical,GastrSymptoms
from .models import UserInfo,PersonalInfo

class IllnessForm(forms.Form):
    metabolic_stress = forms.MultipleChoiceField(
        label="Any previous illnesses?",
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
        label="Any recent changes you've made to your diet?",
        widget=forms.CheckboxSelectMultiple,
        choices=[("sub-optimal solid diet","sub-optimal solid diet"),
    ("Taking liquids only","Taking liquids only"),
    ("Hypo caloric diet","Hypo caloric diet"),
    ("Virtually Nil/Starvation","Virtually Nil/Starvation"),
    ("No change","No change")],
        required=False
    )
   
class GastrSymptomsForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        label="Any Gastrointestinal Symptoms you face?",
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
        label="Any Physical problems?",
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

# class CombinedInfoForm(forms.ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = ['user_id', 'user_name', 'age', 'gender']
#     class Meta:
#         model = PersonalInfo
#         fields = ['height', 'weight', 'weight_lost']
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user_name', 'age', 'gender']
        exclude = ['user_id']

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['weight', 'height','weight_lost']


class SuperuserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Import User model from django.contrib.auth
        fields = ('username', 'email')

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
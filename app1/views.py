from django.shortcuts import render
from django.http import HttpResponse
from .forms import IllnessForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomLoginForm ,DietChangeForm,GastrSymptomsForm,PhysicalForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .models import OtherIllnesses, DietChange, GastrSymptoms, Physical  # Import your models here

def index(request):
    # Your view logic for the 'index' URL pattern
    # Example: render an HTML template
    return render(request, 'app1/home.html')

def about(request):
    # Your view logic for the 'about' URL pattern
    # Example: return a simple text response
    return HttpResponse("This is the about page of app1.")

# def calculate_total_score(selected_illnesses, selected_diet_changes, selected_gastr_symptoms, selected_physical):    # Define a dictionary to map illness names to their scores
#     illness_scores = {
#         "Mental illness": 0,
#         "Minor surgery": 1,
#         "Pregnancy/Lactation": 1,
#         "Pregnancy with complications": 3,
#         "Fever": 1,
#         "Solid tumors/radiotherapy": 1,
#         "Laparoscopic surgeries": 1,
#         "Acute kidney disease": 2,
#         "Cardiac Disease": 2,
#         "Diabetes": 1,
#         "Stroke": 2,
#         "Severe Pneumonia": 2,
#         "Current cancer undergoing treatment": 2,
#         "Transplant surgeries": 3,
#         "Severe Sepsis": 3,
#         "Severe Acute Pancreatitis": 3,
#         "None": 0,
#     }

#     # Define a dictionary to map diet change values to their scores
#     diet_change_scores = {
#         "Low carb diet": 2,
#         "Vegan diet": 3,
#         "Gluten-free diet": 2,
#         "Keto diet": 2,
#         "Mediterranean diet": 1,
#         "No diet changes": 0,
#     }

#     gastr_symptoms_scores={
#         "Nausea":1 ,
#         "Vomiting/Diarrhea":2 ,
#         "Severe Anorexia":3 ,
#         "None":0 ,
#     }
#     physical_scores={
#         "Edema":1,
#         "Muscle Wasting":2,
#         "Fractures":1,
#         "Minor burns":1,
#         "Major burns":2,
#         "Severe burns":3,
#         "Head injury/ Multiple Trauma":3,}
#     # Calculate the total score for selected illnesses

#     # Define dictionaries for scores of selected items (e.g., illness, diet changes, symptoms, and physical)
#     # Replace these dictionaries with your actual data
    
#     total_illness_score = sum(illness_scores.get(illness, 0) for illness in selected_illnesses)
#     total_diet_change_score = sum(diet_change_scores.get(diet_changes, 0) for diet_changes in selected_diet_changes)
#     total_symptoms_score = sum(gastr_symptoms_scores.get(gastr_symptoms, 0) for gastr_symptoms in selected_gastr_symptoms)
#     total_physical_score = sum(physical_scores.get(physical, 0) for physical in selected_physical)
    
#     # Calculate the final total score
#     total_score = (
#         total_illness_score + 
#         total_diet_change_score + 
#         total_symptoms_score + 
#         total_physical_score
#     )
    
#     return total_score

# def illness_form(request):
#     if request.method == 'POST':
#         diet_change_form = DietChangeForm(request.POST)
#         illness_form = IllnessForm(request.POST)
#         gastr_symptoms_form = GastrSymptomsForm(request.POST)
#         physical_form = PhysicalForm(request.POST)

#         if (
#             diet_change_form.is_valid() and 
#             illness_form.is_valid() and 
#             gastr_symptoms_form.is_valid() and 
#             physical_form.is_valid()
#         ):
#             selected_illnesses = illness_form.cleaned_data.get('metabolic_stress')
#             selected_diet_changes = diet_change_form.cleaned_data.get('metabolic_stress')
#             selected_gastr_symptoms = gastr_symptoms_form.cleaned_data.get('gastr_symptoms')
#             selected_physical = physical_form.cleaned_data.get('physical')

#             total_score = calculate_total_score(
#                 selected_illnesses, 
#                 selected_diet_changes, 
#                 selected_gastr_symptoms, 
#                 selected_physical
#             )

#             # Process the form data as needed
#             return render(request, 'app1/result_template.html', {'total_score': total_score})
#     else:
#         diet_change_form = DietChangeForm()
#         illness_form = IllnessForm()
#         gastr_symptoms_form = GastrSymptomsForm()
#         physical_form = PhysicalForm()

#     return render(request, 'app1/illness_form_template.html', {
#         'diet_change_form': diet_change_form,
#         'illness_form': illness_form,
#         'gastr_symptoms_form': gastr_symptoms_form,
#         'physical_form': physical_form,
#     })


def calculate_total_score(selected_illnesses, selected_diet_changes, selected_gastr_symptoms, selected_physical):
    # Define dictionaries to map item names to their scores
    illness_scores = {
        item.metabolic_stress: item.m_score for item in OtherIllnesses.objects.all()
    }

    diet_change_scores = {
        item.changes: item.d_score for item in DietChange.objects.all()
    }

    gastr_symptoms_scores = {
        item.symptoms: item.g_score for item in GastrSymptoms.objects.all()
    }

    physical_scores = {
        item.phy_illness: item.p_score for item in Physical.objects.all()
    }

    # Calculate the total score for selected items
    total_illness_score = sum(illness_scores.get(illness, 0) for illness in selected_illnesses)
    total_diet_change_score = sum(diet_change_scores.get(diet_changes, 0) for diet_changes in selected_diet_changes)
    total_symptoms_score = sum(gastr_symptoms_scores.get(gastr_symptoms, 0) for gastr_symptoms in selected_gastr_symptoms)
    total_physical_score = sum(physical_scores.get(physical, 0) for physical in selected_physical)

    # Calculate the final total score
    total_score = (
        total_illness_score +
        total_diet_change_score +
        total_symptoms_score +
        total_physical_score
    )

    return total_score

def illness_form(request):
    if request.method == 'POST':
        diet_change_form = DietChangeForm(request.POST)
        illness_form = IllnessForm(request.POST)
        gastr_symptoms_form = GastrSymptomsForm(request.POST)
        physical_form = PhysicalForm(request.POST)

        if (
            diet_change_form.is_valid() and
            illness_form.is_valid() and
            gastr_symptoms_form.is_valid() and
            physical_form.is_valid()
        ):
            selected_illnesses = illness_form.cleaned_data.get('metabolic_stress')
            selected_diet_changes = diet_change_form.cleaned_data.get('changes')
            selected_gastr_symptoms = gastr_symptoms_form.cleaned_data.get('symptoms')
            selected_physical = physical_form.cleaned_data.get('phy_illness')

            total_score = calculate_total_score(
                selected_illnesses,
                selected_diet_changes,
                selected_gastr_symptoms,
                selected_physical
            )

            # Process the form data as needed
            return render(request, 'app1/result_template.html', {'total_score': total_score})
    else:
        diet_change_form = DietChangeForm()
        illness_form = IllnessForm()
        gastr_symptoms_form = GastrSymptomsForm()
        physical_form = PhysicalForm()

    return render(request, 'app1/illness_form_template.html', {
        'diet_change_form': diet_change_form,
        'illness_form': illness_form,
        'gastr_symptoms_form': gastr_symptoms_form,
        'physical_form': physical_form,
    })





def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('app1:home')  # Always redirect to the 'home' page on successful login
            else:
                # Handle authentication failure
                form.add_error(None, "Please enter a valid username and password.")
    else:
        form = CustomLoginForm()

    return render(request, 'app1/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Print a message to indicate form validity

            user = form.save()
            print("User created:", user)  # Print the user object

            login(request, user)
            print("User logged in")

            return redirect('app1:login')  # Redirect to the login page after signup
        else:
            print("Form is invalid. Errors:", form.errors)  # Print form validation errors

    else:
        form = CustomUserCreationForm()

    return render(request, 'app1/signup.html', {'form': form})


def homepage(request):
    return render(request, 'app1/home.html')
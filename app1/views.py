from django.http import HttpResponse
from .forms import IllnessForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import  CustomLoginForm ,DietChangeForm,GastrSymptomsForm,PhysicalForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .models import OtherIllnesses, DietChange, GastrSymptoms, Physical  # Import your models here
from django.views.generic.edit import CreateView
from .models import UserInfo
from .forms import UserInfoForm,PersonalInfoForm
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from .models import UserInfo, PersonalInfo
from django.shortcuts import render, redirect
from .forms import UserInfoForm, PersonalInfoForm,SuperuserCreationForm

from django.shortcuts import render, redirect

def add_user_info(request):
    user_age = None
    user_weight = None
    user_height = None
    user_lost = None
    user_name=None
    if request.method == 'POST':
        user_info_form = UserInfoForm(request.POST)
        personal_info_form = PersonalInfoForm(request.POST)

        if user_info_form.is_valid() and personal_info_form.is_valid():
            user_info = user_info_form.save()
            personal_info = personal_info_form.save()
            user_age = user_info_form.cleaned_data['age']
            
            user_weight = personal_info_form.cleaned_data['weight']
            user_name = user_info_form.cleaned_data['user_name']
            # Pass the user_name to the context
            
            user_height = personal_info_form.cleaned_data['height']
            user_lost = personal_info_form.cleaned_data['weight_lost']

            user_info.personal_info = personal_info
            user_info.save()
            
            return redirect(reverse('app1:illness_form', kwargs={'user_age': user_age, 'user_height': user_height, 'user_weight': user_weight, 'user_lost': user_lost, 'user_name': user_name}))

    else:
        user_info_form = UserInfoForm()
        personal_info_form = PersonalInfoForm()

    return render(request, 'app1/user_info_form.html', {
        'user_info_form': user_info_form,
        'personal_info_form': personal_info_form,
        'user_age': user_age,
        'user_weight':user_weight,
        'user_height':user_height,
        'user_lost':user_lost,
        'user_name':user_name,
    })


def index(request):
    # Your view logic for the 'index' URL pattern
    # Example: render an HTML template
    return render(request, 'app1/home.html')

def about(request):
    return render(request, 'app1/about.html')

def calculate_total_score( user_age,user_weight,user_height,user_lost,selected_illnesses, selected_diet_changes, selected_gastr_symptoms, selected_physical):    # Define a dictionary to map illness names to their scores
    
    illness_scores = {
        "Mental illness": 0,
        "Minor surgery": 1,
        "Pregnancy/Lactation": 1,
        "Pregnancy with complications": 3,
        "Fever": 1,
        "Solid tumors/radiotherapy": 1,
        "Laparoscopic surgeries": 1,
        "Acute kidney disease": 2,
        "Cardiac Disease": 2,
        "Diabetes": 1,
        "Stroke": 2,
        "Severe Pneumonia": 2,
        "Current cancer undergoing treatment": 2,
        "Transplant surgeries": 3,
        "Severe Sepsis": 3,
        "Severe Acute Pancreatitis": 3,
        "None": 0,
    }

    # Define a dictionary to map diet change values to their scores
    diet_change_scores = {
        "sub-optimal solid diet": 1,
        "Taking liquids only": 2,
        "Hypo caloric diet": 2,
        "Virtually Nil/Starvation": 3,
        "No change": 0,
    }

    gastr_symptoms_scores={
        "Nausea":1 ,
        "Vomiting/Diarrhea":2 ,
        "Severe Anorexia":3 ,
        "None":0 ,
    }
    physical_scores={
        "Edema":1,
        "Muscle Wasting":2,
        "Fractures":1,
        "Minor burns":1,
        "Major burns":2,
        "Severe burns":3,
        "Head injury/ Multiple Trauma":3,}


    if selected_diet_changes is not None:
        total_diet_change_score = sum(diet_change_scores.get(diet_changes, 0) for diet_changes in selected_diet_changes)
    else:
        total_diet_change_score = 0

    if selected_gastr_symptoms is not None:
        total_gastr_symptoms_score = sum(gastr_symptoms_scores.get(symptoms, 0) for symptoms in selected_gastr_symptoms)
    else:
        total_gastr_symptoms_score = 0

    if selected_physical is not None:
        total_physical_score = sum(physical_scores.get(selected_physical, 0) for selected_physical in selected_physical)
    else:
        total_physical_score = 0

    if selected_illnesses is not None:
        total_illness_score=sum(illness_scores.get(illness,0) for illness in selected_illnesses )
    else:
        total_illness_score=0

    total_score = (
        total_illness_score + 
        total_diet_change_score + 
        total_gastr_symptoms_score + 
        total_physical_score
    )
    
    if isinstance(user_age, int):
    # user_age is an integer
        print("user_age is an integer") 
    print(f'user_age: {user_age}')
    print(f'user_weight: {user_weight}')
    print(f'user_height: {user_height}')
    print(f'user_lost: {user_lost}')
    
    if user_age >= 70:
        print("total score should be increased by 1")
        total_score += 1

   
    percentage_lost = (user_lost / user_weight) * 100
    if 5 <= percentage_lost <= 10:
        
        total_score += 1
    elif percentage_lost > 10:
        total_score += 2
        print("total score should be increased by 2")

    
    bmi = (user_weight * 10000) / (user_height ** 2)
    print(f"BMI: {bmi}")  # Add this line for debugging

    if 16.5 <= bmi <= 18.5:
        total_score += 1
    elif bmi < 16.5:
        total_score += 2
    print(f"Total Score after BMI: {total_score}")  # Add this line for debugging


    return total_score




def get_nutritional_message(total_score):
    if total_score < 3:
        return "Well Nourished: No nutritional intervention required and only balanced intake of food items should be ensured."
    elif 3 <= total_score <= 6:
        return "Patient is at risk of malnutrition or has mild Malnutrition: Nutritional intervention is required and regular monitoring is required."
    else:
        return "Moderate to Severely Malnourished: Nutritional intervention required and regular monitoring is required."

def illness_form(request, user_age,user_height,user_weight,user_lost,user_name):
    if isinstance(user_age, int):
    # user_age is an integer
        print("user_age is an integer") 
    print(f'user_age: {user_age}')
    print(f'user_name exists:{user_name}') 
   
    

   
    
    user_info_form = UserInfoForm()
    personal_info_form = PersonalInfoForm()  # Define the form here

    diet_change_form = DietChangeForm()
    illness_form = IllnessForm()
    gastr_symptoms_form = GastrSymptomsForm()
    physical_form = PhysicalForm()

    if request.method == 'POST':
        user_info_form = UserInfoForm(request.POST)
        personal_info_form = PersonalInfoForm(request.POST)
        print("User Info Form Errors:")
        print(user_info_form.errors)
        

        if user_info_form.is_valid() and personal_info_form.is_valid():
            user_info = user_info_form.save()
            personal_info = personal_info_form.save()
            

            # You can associate the two models if needed
            user_info.personal_info = personal_info
            user_info.save()

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
                    user_age,
                    user_weight,
                    user_height,
                    user_lost,
                    selected_illnesses, 
                    selected_diet_changes, 
                    selected_gastr_symptoms, 
                    selected_physical
                )

                # Process the form data as needed
                return render(request, 'app1/result_template.html', {'total_score': total_score})
            else:
                print("Forms are not valid")
        else:
            print("User info forms are not valid")
    
    # Render the illness form
    
    return render(request, 'app1/illness_form_template.html', {
        'diet_change_form': diet_change_form,
        'illness_form': illness_form,
        'gastr_symptoms_form': gastr_symptoms_form,
        'physical_form': physical_form,
        'user_info_form': user_info_form, 
        'personal_info_form':personal_info_form, # Pass the form to the template
        'user_name': user_name,
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

def homepage(request):
    user_count = User.objects.count()
    return render(request, 'app1/homepage.html', {'user_count': user_count})
def create_superuser(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.save()
            login(request, user)
            return redirect('app1:login')  # Redirect to a success page
    else:
        form = SuperuserCreationForm()
    return render(request, 'app1/create_superuser.html', {'form': form})


from django.shortcuts import render
from django.http import HttpResponse
from .forms import IllnessForm
from .models import OtherIllnesses
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm 
from django.shortcuts import redirect
from django.contrib.auth import login
from django.urls import reverse


def index(request):
    # Your view logic for the 'index' URL pattern
    # Example: render an HTML template
    return render(request, 'app1/index.html')

def about(request):
    # Your view logic for the 'about' URL pattern
    # Example: return a simple text response
    return HttpResponse("This is the about page of app1.")

def calculate_total_score(selected_illnesses):
    # Define a dictionary to map illness names to their scores
    illness_scores = {
        "Mental illness": 0,
        "Minor surgery": 1,
        "Pregnancy/Lactation": 1,
        "Pregnancy with complications": 3,
        "Fever": 1,
        "Solid tumors/radiotherapy": 1,
        "Laproscopic surgeries": 1,
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

    total_score = sum(illness_scores.get(illness, 0) for illness in selected_illnesses)
    return total_score


def illness_form(request):
    if request.method == 'POST':
        form = IllnessForm(request.POST)
        if form.is_valid():
            selected_illnesses = form.cleaned_data.get('metabolic_stress')
            total_score = calculate_total_score(selected_illnesses)
            return render(request, 'app1/result_template.html', {'total_score': total_score})
    else:
        form = IllnessForm()

    return render(request, 'app1/illness_form_template.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'app1/login.html'
    success_url = reverse_lazy('home')  # Redirect to the homepage upon successful login
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup_url'] = reverse('app1:signup')  # Include the 'signup' URL in the context
        return context

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage after signup

    else:
        form = CustomUserCreationForm()

    return render(request, 'app1/signup.html', {'form': form})
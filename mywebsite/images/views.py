from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, SignUpForm, SignInForm
from django.contrib.auth import authenticate, login
from .imageOverlay import ImageOverlay
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# No comments, no fuckin problems.

# Seriously though, I should document this.

from PIL import Image, ImageDraw, ImageFont

def index(request):

    # if request.user.is_authenticated:
    return render(request, 'images/homepage.html')

def answer(request):
    return render(request, 'images/answer.html')

def form(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            star_rating = form.cleaned_data['star_rating']
            kwh = form.cleaned_data['kwh']
            model_num = form.cleaned_data['model_num']


            image = ImageOverlay(star_rating, model_num, kwh)
            image.generate_image()

            img_id = image.get_unique_img_id()

            return render(request, 'images/answer.html', {'image': img_id } )
            

    contact_form = ContactForm()
    return render(request, 'images/nice_form.html', {'form': contact_form})

def sign_in (request):

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('images')

            else:
                return HttpResponse('<h1>Mission Failed!</h1>')
    
    form = SignInForm()
    return render(request, 'images/sign in.html', {'form': form }) 



def sign_up (request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           username = form.cleaned_data['username']
           email = form.cleaned_data['email']
           first_name = form.cleaned_data['first_name']
           last_name = form.cleaned_data['last_name']
           password = form.cleaned_data['password']

           user = User.objects.create_user(username, email)
           user.first_name = first_name
           user.last_name = last_name
           user.set_password(password)
           user.save()
    
    form = SignUpForm()
    return render(request, 'images/sign_up.html', {'form': form})







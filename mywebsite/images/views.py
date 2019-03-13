from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, SignUpForm, SignInForm
from django.contrib.auth import authenticate, login
from .imageOverlay import ImageOverlay
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from PIL import Image, ImageDraw, ImageFont

def index(request):
    # if request.user.is_authenticated:

    if request.user.is_authenticated:
        greeting_message = 'Hello, ' + request.user.first_name + '.'
        return render(request, 'images/homepage.html', {'greeting_message': greeting_message})
    else:
        return render(request, 'images/homepage.html', {'greeting_message': 'Welcome!' })

def answer(request):
    return render(request, 'images/answer.html')

def form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            star_rating = form.cleaned_data['star_rating']
            kwh = form.cleaned_data['kwh']
            model_num = form.cleaned_data['model_num']
            primary = form.cleaned_data['primary']
            secondary = form.cleaned_data['secondary']

            image = ImageOverlay(star_rating, model_num, kwh, primary, secondary)
            image.generate_image()

            img_id = image.get_unique_img_id()

            return render(request, 'images/answer.html', {'image': img_id } )


    contact_form = ContactForm()
    return render(request, 'images/nice_form.html', {'form': contact_form})

def sign_in (request):

    if request.method == 'POST':

        # request.POST is the users info they put in the HTML form, so this populates our
        # form class with their data passed in as a parameter.
        form = SignInForm(request.POST)

        # Runs checks on the form data to make sure it's valid (I think this is like that it's not blank,
        # or has invalid characters? I'm not really sure.)
        if form.is_valid():
            # request.POST[''] retrieves that supplied value from the submitted form.
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            # Confirms that user exists in the database.
            if user is not None:
                login(request, user)

                # Redirects to the root page of the images app, which is the homepage.
                return redirect('/images/')

            else:
                return HttpResponse('<h1>Mission Failed!</h1>')

    # Renders the template with the form data - it looks weird being at the bottom down here,
    # but this is where it's supposed to be.
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

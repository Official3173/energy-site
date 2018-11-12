from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, SignUpForm
from django.contrib.auth import authenticate, login
from .imageOverlay import ImageOverlay
#from .models import UserForm
from django.contrib.auth.forms import UserCreationForm



from PIL import Image, ImageDraw, ImageFont

def index(request):
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
    

    return render(request, 'images/sign in.html') 

def sign_up (request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/images/')
    else:
        form = SignUpForm()
    return render(request, 'images/sign_up.html', {'form': form})






'''
    if request.method == 'POST':

        form = UserForm(request.POST)
        
        user = form.save(commit=False)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    user_email = user.email

                    return render(request, 'images/homepage.html', {'email': user_email})

            



    sign_up_form = UserForm()
    return render(request, 'images/sign_up.html', {'sign_up_form': sign_up_form} )
'''






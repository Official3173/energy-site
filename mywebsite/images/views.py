from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import ContactForm
from .imageOverlay import ImageOverlay


from PIL import Image, ImageDraw, ImageFont

def index(request):
    
    my_info = { 'name': 'Mitchell', 'age': '28', 'url': 'admin/'}
    return render(request, 'images/index.html', my_info)

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
            

    form = ContactForm()
    return render(request, 'images/form.html', {'form': form})







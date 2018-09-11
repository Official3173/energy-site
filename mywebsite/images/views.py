from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import ContactForm

def index(request):
    
    my_info = { 'name': 'Mitchell', 'age': '28', 'url': 'admin/'}
    return render(request, 'images/index.html', my_info)

def answer(request):
    return render(request, 'images/answer.html')

def form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            try:
                name = int(name) * 42069
                return render(request, 'images/answer.html', {'answer':name, 'image': '0.5 Stars Final Template' })

            except:
                print('\n' + 'Invalid number entered by user - error page to be displayed' + '\n')
                return HttpResponse('<h1> OWO, looks like u made an oopsie woopsie fucky wucky - make sure you entered an actual number </h1>')

            

    form = ContactForm()
    return render(request, 'images/form.html', {'form': form})







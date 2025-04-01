from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1>')
    

def contact(request):
    return HttpResponse('<h1>Contactez-nous</h1>')
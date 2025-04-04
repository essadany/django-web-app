from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from listings.models import Band
from listings.forms import ContactUsForm, BandForm

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['yassineessaadani20@gmail.com'],
            )
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                'listings/contact.html',
                {'form': form})
    
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})
def about(request):
    return render(request, 'listings/about.html', {'bands': 'band'})

def listings(request):
    return render(request, 'listings/listings.html')
    
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('band-list')
    else:
        form = BandForm()
    return render(request, 'listings/band_form.html', {'form': form})
from django.shortcuts import render, redirect
from app.forms import PortraitForm
from app.models import Portrait


# Create your views here.

def accueil(request):
    return render(request, 'app/index.html')

def portraits(request):
    portraits = Portrait.objects.all()
    context = {
        "portraits":portraits
    }
    return render(request, 'app/portraits.html', context)

def administration(request):
    form = PortraitForm(request.POST, request.FILES)
    portraits = Portrait.objects.all()
    message = ''
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            message = "Portrait ajouté avec succès"
            return redirect('portraits')

    context = {
        "form":form,
        "message":message,
        "portraits":portraits
    }
    return render(request, 'app/admin.html', context)

def single_portrait(request, id):
    portrait = Portrait.objects.get(id=id)
    form = PortraitForm(instance=portrait)
    message = ''
    if request.method == 'POST':
        form = PortraitForm(request.POST, request.FILES, instance=portrait)
        if form.is_valid():
            form.save()
            message = "Portrait ajouté avec succès"
            return redirect('portraits')

    context = {
        "form":form,
        "message":message
    }
    return render(request, 'app/single-portrait.html', context)

def delete(request, id):
    portrait = Portrait.objects.get(id=id)
    portrait.delete()
    return redirect('administration')
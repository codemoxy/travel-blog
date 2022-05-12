from django.shortcuts import render


def HomePage(request):
    return render(request, template_name='index.html')

def AboutPage(request):
    return render(request, template_name='about.html')

def ContactPage(request):
    return render(request, template_name='contact.html')

def GalleryPage(request):
    return render(request, template_name='gallery.html')
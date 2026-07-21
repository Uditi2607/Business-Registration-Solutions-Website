from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'about/about.html')

def services(request):
    return render(request, 'services/services.html')

def blog(request):
    return render(request, 'blog/blog.html')

def contact(request):
    return render(request, 'contact/contact.html')

def faq(request):
    return render(request, 'faq/faq.html')

def privacy(request):
    return render(request, 'privacy/privacy.html')

def terms(request):
    return render(request, 'terms/terms.html')

def refund(request):
    return render(request, 'refund/refund.html')
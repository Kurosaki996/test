from django.shortcuts import render
from apps.main.models import Index, Steps, Contact

# Create your views here.
def index(request):
    settings_id = Index.objects.latest("id")
    settings_all = Steps.objects.all()
    return render(request, 'base/index.html', locals())

def about(request):
    return render(request, 'base/about-us.html', locals())

def contact(request):
    contact = Contact.objects.latest("id")
    return render(request, 'base/contacts.html', locals())

def about_me(request):
    return render(request,'base/about-me.html', locals())



# def faq(request):
#     faq = Faq.objects.all()
#     return render(request, 'faq.html', locals())
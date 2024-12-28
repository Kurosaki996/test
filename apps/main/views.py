from django.shortcuts import render
from apps.main.models import Settings, Settings_All

# Create your views here.
def index(request):
    settings_id = Settings.objects.latest("id")
    settings_all = Settings_All.objects.all()
    return render(request, 'base/index.html', locals())
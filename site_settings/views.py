from django.http import HttpResponse
from django.shortcuts import render
from site_settings.models import Setting


def show_settings(request):
    settings = Setting.objects.all()
    text_response = ""
    for setting in settings:
        text_response += str(setting) + "<br/>"
    return HttpResponse(text_response)


def home(request):
    my_list = Setting.objects.filter(selected=True) == []
    if my_list:
        setting = ''
    else:
        setting = Setting.objects.filter(selected=True)[0]
    context = {
        'theme': setting,
    }
    return render(request, 'index.html', context)

from django.urls import path
import site_settings.views as view

app_name = 'site_settings'

urlpatterns = [
    path('show/', view.show_settings, name='show'),
]

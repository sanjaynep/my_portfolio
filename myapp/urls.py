from myapp.views import index, download_resume
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('download-resume/', download_resume, name='download_resume'),

]

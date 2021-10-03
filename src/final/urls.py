from django.urls import path
from .views import (
    my_fbv, FinalView
)


app_name = 'final'
urlpatterns = [
    path('', FinalView.as_view(template_name='contact.html'), name='final-list')
]
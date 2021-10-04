from django.urls import path
from .views import (
    my_fbv, FinalView,
    FinalListView
)


app_name = 'final'
urlpatterns = [
    path('', FinalView.as_view(template_name='contact.html'), name='final-list'),
    path('<int:id>/', FinalView.as_view(), name='final-detail'),
    path('<int:id>/', FinalListView.as_view(), name='final-list')
]
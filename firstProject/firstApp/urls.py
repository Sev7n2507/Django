from django.urls import path
from . import views

app_name = 'firstApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_question, name='create_question'),
    path('<id>', views.detail_question),
    path('<id>/update/', views.update_question),
    path('<id>/delete/', views.delete_question),
]

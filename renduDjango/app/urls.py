from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('create/', views.create_product, name='create_product'),
    path('<int:id>', views.detail_product, name='detail_product'),
    path('<int:id>/update/', views.update_product, name='update_product'),
    path('lobby', views.lobby, name='lobby'),
]

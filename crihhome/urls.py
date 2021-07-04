from django.urls import path
from .views import (
            home,
            post_detail,
)


app_name = 'crihhome'
urlpatterns = [
    path('', home, name='homepage'),
    path('<int:pk>/<str:slug>/', post_detail, name='post_detail'),


]
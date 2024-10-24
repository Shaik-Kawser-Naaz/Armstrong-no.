from django.urls import path
from app1 import views
urlpatterns=[
    path('arm',views.func1,name="an")
]
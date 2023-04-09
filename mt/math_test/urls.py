from django.urls import path
from .views import *

urlpatterns = [
    path('', provide_page, name="Main"),
    path('gq/', get_quiz_test, name="gqt")
]

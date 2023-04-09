from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', provide_page, name="Main"),
    path('get_quiz/', get_quiz_test, name='gqt'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


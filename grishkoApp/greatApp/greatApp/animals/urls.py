from django.urls import path, include
from greatApp.animals.views import add_animal, details_animal, edit_animal, delete_animal


urlpatterns = [
    path('add/', add_animal, name='add animal'),
    path('<str:username>/animal/<slug:animal_slug>/', include([
        path('', details_animal, name='animal details'),
        path('edit/', edit_animal, name='edit animal'),
        path('delete/', delete_animal, name='delete animal'),
    ])),
]

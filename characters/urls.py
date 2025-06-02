from django.urls import path
from rest_framework.routers import DefaultRouter

from characters.views import get_random_characters_view, CharacterListView

app_name = "characters"
urlpatterns = [
    path("characters/random/", get_random_characters_view, name="characters_random"),
    path("characters/", CharacterListView.as_view(), name="characters_list"),
]

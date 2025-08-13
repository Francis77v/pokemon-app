from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, PokeBallViewSet, HomeView, get_item, catch_pokemon, list_pokeballs, BagView

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet)
router.register(r'pokeball', PokeBallViewSet)

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('bag/', BagView.as_view(), name='bag'),
    path('api/get-item/', get_item, name='get_item'),
    path('api/catch-pokemon/', catch_pokemon, name='catch_pokemon'),
    path('api/pokeballs/', list_pokeballs, name='list_pokeballs'),  # NEW
    path('api/', include(router.urls)),
]

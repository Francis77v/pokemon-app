
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Pokemon, PokeBall
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Pokemon, PokeBall
from .serializers import PokemonSerializer, PokeBallSerializer


# POST /api/get-item/
@api_view(['POST'])
def get_item(request):
    name = request.data.get('name')
    if not name:
        return Response({'error': 'No item name provided.'}, status=400)

    pokeball, created = PokeBall.objects.get_or_create(name=name)
    serializer = PokeBallSerializer(pokeball)
    return Response(serializer.data, status=201 if created else 200)

@api_view(['POST'])
def get_item(request):
    name = request.data.get('name')
    if not name:
        return Response({"error": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Save the Pokéball
    ball = PokeBall.objects.create(name=name)
    serializer = PokeBallSerializer(ball)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# POST /api/catch-pokemon/
@api_view(['POST'])
def catch_pokemon(request):
    name = request.data.get('name')
    types = request.data.get('types')
    species = request.data.get('species', 'Unknown')
    ability = request.data.get('ability', 'Unknown')

    if not name or not types:
        return Response({'error': 'Missing required Pokémon data.'}, status=400)

    # Find a free pokeball
    try:
        free_ball = PokeBall.objects.filter(pokemon__isnull=True).first()
        if not free_ball:
            return Response({'error': 'No available Pokéballs.'}, status=400)

        # Create Pokémon
        pokemon = Pokemon.objects.create(
            name=name,
            types=types,
            species=species,
            ability=ability,
        )

        # Assign Pokémon to Pokéball
        free_ball.pokemon = pokemon
        free_ball.save()

        return Response({'message': f'{name} caught successfully!'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])

def list_pokeballs(request):
    pokeballs = PokeBall.objects.all()
    serializer = PokeBallSerializer(pokeballs, many=True)
    return Response(serializer.data)

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokeBallViewSet(viewsets.ModelViewSet):
    queryset = PokeBall.objects.all()
    serializer_class = PokeBallSerializer

class HomeView(TemplateView):
    template_name = 'dashboard.html'

class BagView(TemplateView):
    template_name = 'Bag.html'
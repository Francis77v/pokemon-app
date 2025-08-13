from rest_framework import serializers
from .models import Pokemon, PokeBall

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'types', 'ability', 'species']


class PokeBallSerializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer(read_only=True)  # nested serializer, read-only

    class Meta:
        model = PokeBall
        fields = '__all__'
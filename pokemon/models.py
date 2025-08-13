from django.db import models

# # Create your models here.
# class Bag(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False)
#     date_created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'dev"."pokemon_dev'  # Force schema.table

class Pokemon(models.Model):
    name = models.CharField(max_length=150)
    types = models.CharField(max_length=250)
    species = models.CharField(max_length=150)
    ability = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

class PokeBall(models.Model):
    name = models.CharField(max_length=150)
    # bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    pokemon = models.OneToOneField(Pokemon, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)

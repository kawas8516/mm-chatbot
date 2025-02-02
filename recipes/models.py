from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.JSONField()  # e.g., ["tomato", "onion", "bread"]
    instructions = models.TextField()
    cuisine = models.CharField(max_length=255)
    prep_time = models.IntegerField(help_text="Time in minutes")
    nutrition_info = models.JSONField(default=dict)  # e.g., {"calories": 200, "protein": "10g"}

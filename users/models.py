from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    dietary_preferences = models.JSONField(default=dict)  # e.g., {"vegan": True, "gluten_free": False}
    saved_recipes = models.ManyToManyField("recipes.Recipe", blank=True)
    preferred_cuisine = models.CharField(max_length=255, blank=True, null=True)

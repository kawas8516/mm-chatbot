from django.db import models

# Create your models here.
class Recommendation(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    recommended_recipe = models.ForeignKey("recipes.Recipe", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

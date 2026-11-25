
from django.db import models


class FoodItem(models.Model):

    # Primary Key
    id = models.AutoField(primary_key=True)

    # Food Details
    item_name = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.FloatField()
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'food_menu_items'

    def __str__(self):
        return self.item_name
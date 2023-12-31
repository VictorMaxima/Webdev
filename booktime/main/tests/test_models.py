from decimal import Decimal
from django.test import TestCase
from main import models

class TestModels(TestCase):
    def test_active_manager_works(self):
        models.Product.objects.create(
            name="The cathedraland the bazaar",
            price=Decimal("10.00")
        )
        models.Product.objects.create(
            name="Pride and Prejudice",
            price=Decimal("2.00")
        )
        models.Product.objects.create(
            name="A Tale of Two Ciities",
            price=Decimal("2.00"),
            active=False
        )
        self.assertEqual(len(models.Product.objects.active()),2)
from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title='Tomato soup',
            price=3.45,
            inventory=15
        )

        itemstr = item.get_item()

        self.assertEqual(item.title, 'Tomato soup')
        self.assertEqual(item.price, 3.45)
        self.assertEqual(item.inventory, 15)
        self.assertEqual(itemstr, "Tomato soup : 3.45")

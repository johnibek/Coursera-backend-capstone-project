from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token
from restaurant.models import Menu
from api.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.hamburger = Menu.objects.create(title='Hamburger', price=3.45, inventory=15)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()

    def test_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('menu_items'))

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.hamburger.title)
        self.assertContains(response, self.hamburger.price)
        self.assertContains(response, self.hamburger.inventory)

from django.test import TestCase
from restaurant.models import Menu,Booking
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        Menu.objects.create(title='Grilled Beef Meat',price=8.0,inventory=6)
        Menu.objects.create(title= 'Eyebeef',price=10.5,inventory=30)


    def test_getall(self):
            # get all Menu objects using the API
        url = reverse('menu')
        response = self.client.get(url)
        # check if the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # serialize the retrieved objects and compare them with the expected data
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
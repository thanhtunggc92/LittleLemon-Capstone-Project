from django.test import TestCase
from restaurant.models import Menu,Booking

class MenuTest(TestCase):

    @classmethod
    def test_get_item(cls):
        cls.menu = Menu.objects.create(title="IceCream", price=80, inventory=100)
        #  = Menu.objects.create(title="DarkChocolate", price=100, inventory=110)



    def tes_field(self):
        self.assertIsInstance(self.menu.title,str)
        self.assertIsInstance(self.menu.price,int)
        # self.assertEqual(str(item2),'WhiteChocolate : 90')
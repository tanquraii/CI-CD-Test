from django.test import TestCase
from .models import CatUser

class CatUserModelTest(TestCase):
    def test_model_creation(self):
        obj = CatUser.objects.create(nickname='stalkery', password=123)
        
        # Test if the object was created successfully
        self.assertEqual(obj.nickname, 'stalkery')
        self.assertEqual(obj.password, 123)
        
    def test_another_thing(self):
        # Another test
        self.assertTrue(True)  # Example test that always passes


# Create your tests here.

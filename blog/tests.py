from django.test import TestCase
from .models import Category
from django.utils import timezone

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title='Test Category',
            descripation='This is a test category',
            url='test-category',
            image='category/test_image.jpg',
            add_date=timezone.now()
        )
        
    def test_category_creation(self):
        self.assertEqual(self.category.title, 'Test Category')
        self.assertEqual(self.category.descripation, 'This is a test category')
        self.assertEqual(self.category.url, 'test-category')
          
        
    
    def test_str_method(self):
        self.assertEqual(str(self.category),'Test Category')
        
    def test_add_date_auto_now_add(self):
        self.assertIsNotNone(self.category.add_date)    
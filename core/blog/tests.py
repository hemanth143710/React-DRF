from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category
# Create your tests here.

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.object.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

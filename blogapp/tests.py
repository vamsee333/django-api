from django.test import TestCase
from rest_framework.test import APITestCase
# Create your tests here.

from django.contrib.auth.models import User
from .models import Blogpost

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj=User(username='newuser',email='newuser@test.com')
        user_obj.set_password('123abc@')
        user_obj.save()
        blog_post=Blogpost.objects.create(user=user_obj,title='hello world',content='test data')

    def test_single_user(self):
        obj=User.objects.count()
        self.assertEqual(obj,1)

    def test_single_post(self):
        post_obj=Blogpost.objects.count()
        self.assertEqual(post_obj,1)

    def test_blog_title(self):
        post_data=Blogpost.objects.get(pk=1)
        if post_data.title=='hello world':
            print ('sucess')
        print ('invalid title but test passed')






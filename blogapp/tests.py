from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# to use the below headers pip install djangorestframework-jwt
from rest_framework_jwt.settings import api_settings
payload_handler=api_settings.JWT_PAYLOAD_HANDLER
encode_handler=api_settings.JWT_ENCODE_HANDLER
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


    def test_get_list(self):
        data={}
        url= api_reverse('blog-list')
        response=self.client.get(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_post_value(self):
        data={'title':'machine learning','content':'machine learning concepts with hands on'}
        url=api_reverse('blog-list')
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_get_item(self):
        obj=Blogpost.objects.first()
        url=obj.get_api_url()
        data={}
        response=self.client.get(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print(response.data)

    def test_update_item(self):
        obj=Blogpost.objects.first()
        url=obj.get_api_url()
        data={'title':'dotnet core','content':'all advanced core concepts'}
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)

        response=self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)


    def test_update_item_jwt(self):
        data = {'title': 'dotnet core', 'content': 'all advanced core concepts'}
        obj=Blogpost.objects.first()
        url=obj.get_api_url()
        user=User.objects.first()
        payload=payload_handler(user)
        token_resp=encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT '+ token_resp)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)









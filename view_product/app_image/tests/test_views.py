from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from app_image.models import CommentModel, ReplyModel

class TestViews(TestCase):
    
    def test_project_list_GET(self):
        client=Client()
        response=client.get(reverse('app_image:viewProduct'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'app_image/viewProduct.html')

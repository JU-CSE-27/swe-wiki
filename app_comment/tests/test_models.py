from django.test import TestCase
from app_comment.models import CommentModel,ReplyModel
from django.contrib.auth.models import User

class TestAppModels(TestCase):
    def test_model_str(self):
        user=User.objects.create(username="testuser", password="12345")
        m_comments=CommentModel.objects.create(user=user, m_comments="My watch is like as image")
        self.assertEqual(str(m_comments),"My watch is like as image")

    def test_model_reply(self):
        user=User.objects.create(username="testuser", password="12345")
        m_comments=CommentModel.objects.create(user=user,m_comments="My watch is like as image")
        m_reply=ReplyModel.objects.create(user=user,m_comment=m_comments,m_reply="You are lucky")

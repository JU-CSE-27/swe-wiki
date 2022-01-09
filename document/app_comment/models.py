from django.db import models
from django.contrib.auth.models import User


"""
There are two models- CommentModel,ReplyModel

"""

class CommentModel(models.Model):
     """
	:model name: CommentModel
    :inherit: models.Model
    """
     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
     m_comments=models.TextField()
     m_comment_date=models.DateTimeField(auto_now_add=True)
     def __str__(self):
         return self.m_comments




# Create model for reply
class ReplyModel(models.Model):
     """
	:model name: ReplyModel
    :inherit: models.Model
    """
     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_reply')
     m_comment=models.ForeignKey(CommentModel,on_delete=models.CASCADE,related_name='reply_comment')
     m_reply=models.TextField()
     m_reply_date=models.DateTimeField(auto_now_add=True, null=True)

     def __str__(self):
         return self.m_reply

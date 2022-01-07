from django.db import models
from django.contrib.auth.models import User

# Create model for comment

class CommentModel(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
     m_comments=models.TextField()
     m_comment_date=models.DateTimeField(auto_now_add=True)
     def __str__(self):
         return self.m_comments




# Create model for reply
class ReplyModel(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_reply')
     m_comment=models.ForeignKey(CommentModel,on_delete=models.CASCADE,related_name='reply_comment')
     m_reply=models.TextField()

     def __str__(self):
         return self.m_reply

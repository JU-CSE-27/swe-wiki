from django import forms
from app_comment.models import CommentModel, ReplyModel
#comment form is created
class commentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields=('m_comments',)
#reply form is created
class replyForm(forms.ModelForm):
    class Meta:
        model=ReplyModel
        fields=('m_reply',)

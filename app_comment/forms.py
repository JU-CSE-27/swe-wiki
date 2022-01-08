from django import forms
from app_comment.models import CommentModel, ReplyModel

"""
There are two form - commentForm,replyForm

"""

class commentForm(forms.ModelForm):
    """
	:form name:commentForm
    :inherit: forms.ModelForm
    """
    
    class Meta:
        model=CommentModel
        fields=('m_comments',)


class replyForm(forms.ModelForm):
    """
	:form name:replyForm
    :inherit: forms.ModelForm
    """
 
    class Meta:
        model=ReplyModel
        fields=('m_reply',)

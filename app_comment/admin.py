from django.contrib import admin
from app_comment.models import CommentModel,ReplyModel
# Register your models here.
admin.site.register(CommentModel)
#admin.site.register(UserLikeModel)
#admin.site.register(UnlikeModel)
admin.site.register(ReplyModel)

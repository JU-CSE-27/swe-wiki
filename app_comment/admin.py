from django.contrib import admin
from app_comment.models import CommentModel,ReplyModel
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    model=CommentModel
    list_display=('excerpt',)
    def excerpt(self,obj):
        return obj.get_excerpt(5)

class ReplyAdmin(admin.ModelAdmin):
    model=ReplyModel
    list_display=('excerpts',)
    def excerpts(self,obj):
        return obj.get_excerpts(5)
admin.site.register(CommentModel,CommentAdmin)
#admin.site.register(UserLikeModel)
#admin.site.register(UnlikeModel)
admin.site.register(ReplyModel,ReplyAdmin)

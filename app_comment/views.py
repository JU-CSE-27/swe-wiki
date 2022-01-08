from django.shortcuts import render , HttpResponseRedirect
from app_comment.models import CommentModel,ReplyModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from app_comment.forms import commentForm,replyForm

"""
This is a review page
Function name is comment_page
"""

def comment_page(request):
    """
    :param name: request
    :param type: URL
    :return:URL,Dictionary
    """

    formComment=commentForm()
    formReply=replyForm()
    allComment=CommentModel.objects.all()
   


    if request.method=='POST':
        formComment = commentForm(request.POST)
        formReply = replyForm(request.POST)
        if formComment.is_valid():
            commentAdd=formComment.save(commit=False)
            commentAdd.user=request.user
            commentAdd.save()
            return HttpResponseRedirect(reverse('app_comment:comment'))

        if formReply.is_valid():
            replyAdd= formReply.save(commit=False)
            replyAdd.user=request.user
            parentId = int(request.POST.get('parent_id'))
            assignComment=CommentModel.objects.get(id=parentId)
            replyAdd.m_comment=assignComment
            replyAdd.save()
            return HttpResponseRedirect(reverse('app_comment:comment'))



    return render(request,'app_comment/comment.html',context={ 'comment_form':formComment,'allComment':allComment,'reply_form':formReply})


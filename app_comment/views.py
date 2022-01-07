from django.shortcuts import render , HttpResponseRedirect
from app_comment.models import CommentModel,ReplyModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from app_comment.forms import commentForm,replyForm

# Create your views here.

def comment_page(request):

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


"""def reply_page(request,id):

    formReply=replyForm()
    assignComment=CommentModel.objects.get(pk=id)
    allReply=ReplyModel.objects.filter(m_comment=assignComment)

    if request.method=='POST':
        formReply = replyForm(request.POST)
        if  formReply.is_valid():
            replyAdd= formReply.save(commit=False)
            replyAdd.user=request.user
            replyAdd.save()
            return HttpResponseRedirect(reverse('app_comment:comment',kwargs={'id':id}))



    return render(request,'app_comment/comment.html',context={ 'reply_form':formReply,'allReply':allReply})"""


"""
@login_required
def liked_page(request, pk):
    userComment = CommentModel.objects.get(pk=pk)
    alreadyLiked = LikeModel.objects.filter(m_comment=userComment)
    if not alreadyLiked:
        likedPost = LikeModel(m_comment=userComment)
        likedPost.save()
    return HttpResponseRedirect(reverse('app_comment:comment', kwargs={'id':userComment.id}))"""

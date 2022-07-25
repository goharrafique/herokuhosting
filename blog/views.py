from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,Blogcomment
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
# Create your views here.
def blogHome(request):
    allPost=Post.objects.all()
    # print(allPost)
    context={'allPost':allPost}
    # return render(request, 'index.html')
    return render(request, 'blog/blogHome.html',context)

  
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    
    post.views=post.views+1
    post.save()
    
    comments=Blogcomment.objects.filter(post=post,parent=None)
    replies=Blogcomment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)    
    # print(comments, replies)
    # print(replyDict)
    context={"post":post,'comments':comments,'user': request.user,'replyDict': replyDict}
    # return render(request, 'index.html')
    # return HttpResponse(f"THis is slug page :{slug}")
    return render(request, 'blog/blogPost.html',context)
def postComment(request):
    if request.method=="POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno=request.POST.get('postSno')
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get('parentSno')
        if parentSno=='':
          comment=Blogcomment(comment=comment,user=user,post=post)
          comment.save()
          messages.success(request, 'comment is posted')
        else:
            parent=Blogcomment.objects.get(sno=parentSno)  
            comment=Blogcomment(comment=comment,user=user,post=post,parent=parent)
            messages.success(request, 'reply  comment is posted')
            comment.save()
        # messages.success(request, 'comment is posted')
    return redirect(f'/blog/{post.slug}')
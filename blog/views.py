from django.shortcuts import render,HttpResponse
from blog.models import Post

# Create your views here.
def blogHome(request):
    allPost=Post.objects.all()
    # print(allPost)
    context={'allPost':allPost}
    # return render(request, 'index.html')
    return render(request, 'blog/blogHome.html',context)
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    # print(post)
    context={"post":post}
    # return render(request, 'index.html')
    # return HttpResponse(f"THis is slug page :{slug}")
    return render(request, 'blog/blogPost.html',context)
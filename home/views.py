from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def contact(request):
    # messages.error(request, 'Welcome to contact')
    if request.method=='POST':
        # print("we are using the post request the post method")
        name=request.POST['name']
        email=request.POST['email']
        content=request.POST["content"]
        # print(name, email, content)
        if len(name)<2 or len(email)<3 or len(content)<4:
            messages.error(request, 'please fill corrent ')
        else:    
         contant=Contact(name=name,email=email,content=content)
         contant.save()
         messages.success(request, 'your message has been sent')
    return render(request, 'home/contact.html')
   
def about(request):
    # return render(request, 'index.html')
 return render(request, 'home/about.html')
def home(request):
    # return render(request, 'index.html')
 return render(request, 'home/home.html')

def search(request):
    query=request.GET['query']
    if len(query)>30:
        allPost=Post.objects.none()
    # params={'allPost':allPost}
    # allPost=Post.objects.all()
    else:
     allPosttitle=Post.objects.filter(title__icontains=query)
     allPostAdd=Post.objects.filter(content__icontains=query)
     allPost=allPosttitle.union(allPostAdd)
    if allPost.count() == 0:
         messages.error(request, 'please fill corrent ') 
    params={"allPost":allPost, 'query':query}
    return render(request, "home/search.html",params)
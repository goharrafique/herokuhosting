from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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


def handleSign(request):
    if request.method=="POST":
       fullName= request.POST['name']
       email= request.POST['email']
       pass1= request.POST['password']
       pass2= request.POST['Cpassword']
       username= request.POST['username']
       
       #check for validate
       if not username.isalnum():
           messages.error(request, 'username should be isalnum')
           return redirect('/')
       if pass1 !=pass2:
           messages.error(request, 'password not matching')    
           return redirect('home')
       #create the user
       myuser=User.objects.create_user(username,email,pass1)
       myuser.first_name=fullName
       myuser.save()
       messages.success(request, 'Your icoder account has been created')
       return redirect('/')
    else:
        return HttpResponse("404- Not Found")
    
def handleLogin(request):
    if request.method=="POST":
        loginuser=request.POST['loguser']
        loginpass=request.POST['Logpass']
        user=authenticate(username=loginuser,password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "successfully login")
            return redirect('home')
        else:
            messages.error(request,'invalid credentials')
            return redirect('home')
    return HttpResponse('heloo login')
def handleLogout(request):
    
    logout(request)
    messages.success(request, 'successfully logout')
    return redirect('home')
    return HttpResponse('heloo login')


#fetch top post on home on the basis of number of views
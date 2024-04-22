from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from .forms import UserRegistrationForm

# Create your views here.
rooms=[
    {'id':1, 'name':'lets learn python'},
    {'id':2, 'name':'django'},
    {'id':3, 'name':'sql database'},
]



def loginPage(request):
    
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,'Incorrect login credentials')
            
    context={'page':page}
    return render(request,'base/loginpage.html',context)


def logoutuser(request):
    logout(request)
    return redirect('home')

def registeruser(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,'Error in Registration,Try again!')

    return render(request,'base/loginpage.html',{'form':form}) 




def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
    Q(city__icontains=q) |
    Q(title__icontains=q) |
    Q(location__icontains=q) |
    Q(description__icontains=q) |
    Q(host__username__icontains=q) |
    Q(category__icontains=q) |
    Q(state__icontains=q) |
        (Q(city__icontains=q) & Q(title__icontains=q)) |
        (Q(city__icontains=q) & Q(category__icontains=q))
        

    )

    post_count = posts.count()
    flag = True
    categories = ['Gigs','Rentals','Events','Jobs','News','Meetings','Services','For sale','Activity Partner']
    statelist = ['Kerala','Tamil Nadu','Karnataka','New Delhi']
    context = {'posts': posts,'post_count':post_count,'categories': categories,'statelist':statelist,'flag':flag} 
    return render(request,'base/home.html',context)

def post(request,pk):
    post = Post.objects.get(id=pk)      
 
    context = {'post':post}

    return render(request,'base/post.html',context)


@login_required(login_url='login')
def createPost(request):

    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.host = request.user
            
            post.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request,'base/postform.html',context)


def updatePost(request,pk):

    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request,'base/postform.html',context)

#@login_required('loginu')
def deletePost(request,pk):
     post = Post.objects.get(id=pk)
     if request.method == 'POST':
         post.delete()
         return redirect('home')
     
     return render(request, 'base/delete.html',{'obj':post})

        
def myposts(request):

    if request.method == 'GET':
        post = Post.objects.filter(host=request.user)
        categories = ['Gigs','Rentals','Events','Jobs','News','Meetings','Services','For sale','Activity Partner']
        statelist = ['Kerala','Tamil Nadu','Karnataka','New Delhi']
        flag = False
        context = {'posts': post,'categories': categories,'statelist':statelist,'flag':flag} 
        return render(request,'base/home.html',context)



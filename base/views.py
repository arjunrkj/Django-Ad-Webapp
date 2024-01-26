from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
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
    rooms=Room.objects.filter(
        Q(city__icontains=q) | 
        Q(title__icontains=q) | 
        Q(location__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q) |
        Q(category__icontains=q) |
        Q(state__icontains=q) |
        (Q(city__icontains=q) & Q(title__icontains=q)) |
        (Q(category__icontains=q) & Q(city__icontains=q))

    )

    room_count = rooms.count()
    flag = True
    categories = ['Gigs','Rentals','Events','Jobs','News','Meetings','Services','For sale','Activity Partner']
    statelist = ['Kerala','Tamil Nadu','Karnataka','New Delhi']
    context = {'rooms': rooms,'room_count':room_count,'categories': categories,'statelist':statelist,'flag':flag} 
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)      
 
    context = {'room':room}

    return render(request,'base/room.html',context)


@login_required(login_url='login')
def createRoom(request):

    form = RoomForm   
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            room.host = request.user
            
            room.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request,'base/roomform.html',context)


def updateRoom(request,pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request,'base/roomform.html',context)

#@login_required('loginu')
def deleteRoom(request,pk):
     room= Room.objects.get(id=pk)
     if request.method == 'POST':
         room.delete()
         return redirect('home')
     
     return render(request, 'base/delete.html',{'obj':room})

        
def myposts(request):

    if request.method == 'GET':
        room = Room.objects.filter(host=request.user)
        categories = ['Gigs','Rentals','Events','Jobs','News','Meetings','Services','For sale','Activity Partner']
        statelist = ['Kerala','Tamil Nadu','Karnataka','New Delhi']
        flag = False
        context = {'rooms': room,'categories': categories,'statelist':statelist,'flag':flag} 
        return render(request,'base/home.html',context)



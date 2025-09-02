from django.shortcuts import render, redirect
from .models import Posts
from django.contrib.auth.models import User, auth
from django.contrib import messages




# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Posts.objects.get(id=pk)
    return render(request, 'post.html', {'posts':posts})

def createpost(request):
    if request.method == 'POST':
        title = request.POST['title']
        newpost = request.POST['newpost']
        post_created = Posts(title=title, body=newpost)
        post_created.save()
        return redirect('index')
    else:
        # If the request method is GET, render the create post form   
        return render(request, 'createpost.html')
    
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = User.objects.get(email=email)
            user = auth.authenticate(username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        email = request.POST['email']

        if password1==password2:
                

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, 'Email exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
        else:
            messages.info(request, 'Password unmatch')
            return redirect('register')
    
    return render(request, 'register.html')
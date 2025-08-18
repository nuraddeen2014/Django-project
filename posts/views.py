from django.shortcuts import render, redirect
from .models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Posts.objects.get(id=pk)
    return render(request, 'post.html', {'posts':posts})

def createpost(request):
    if request. method == 'POST':
        title = request.POST['title']
        newpost = request.POST['newpost']
        post_created = Posts(title=title, body=newpost)
        post_created.save()
        return redirect('index')
    else:
        # If the request method is GET, render the create post form   
        return render(request, 'createpost.html')
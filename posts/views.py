
from http import server
from .forms import PostFormCreate, PostFormUpdate
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from django.db.models import Q


from .models import Post

def home(request):

    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
        try:
            posts = Post.objects.filter(Q(id = search_query) | Q(user_id = search_query))
        except:
            return HttpResponse("Id is incorrect make sure that you pass number")

    if search_query == "":
        posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, "posts/posts.html", context )




def post_create(request):
    form = PostFormCreate()

    if request.method == "POST":
        users_id = []
        users = requests.get("https://jsonplaceholder.typicode.com/users")
        users = users.json()

        for user in users:
            users_id.append(user["id"])
        
        if int(request.POST["user_id"]) in users_id:
            pass
        else:
            return HttpResponse("User with this Id does not exists")


        form = PostFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form":form}
    return render(request, "posts/post_create_update.html", context )


def post_update(request, pk):
    post = Post.objects.get(id = pk)
    form = PostFormUpdate(instance=post)
    

    if request.method == "POST":
        form = PostFormUpdate(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form":form}
    return render(request, "posts/post_create_update.html", context )

def post_delete(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return redirect("home")
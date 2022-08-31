from posts.models import Post
import requests
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer, PostSerializerUpdate


@api_view(["GET"])
def get_routes(request):
    routes = [
        {"GET":"/api/posts"},
        {"POST":"/api/posts"},
        {"GET":"/api/posts/id"},
        {"PUT":"/api/posts/id"},
        {"DELETE":"/api/posts/id"},
        {"GET":"/api/posts/users/id"},
    ]

    return Response(routes)


@api_view(["GET","POST"])
def posts(request):

    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    
    if request.method == "POST":
        users_id = []
        users = requests.get("https://jsonplaceholder.typicode.com/users")
        users = users.json()
        
        for user in users:
            users_id.append(user["id"])
            
        if request.data["user_id"] in users_id:
            pass
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    posts = posts.json()
    return Response(posts)


@api_view(["GET","PUT","DELETE"])
def post(request,pk):


    if request.method == "GET":
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post,many=False)
        except:
            post = requests.get(f"https://jsonplaceholder.typicode.com/posts/{pk}")
            post = post.json()
            try:
                create_post = Post.objects.create(
                user_id = post["userId"],
                body = post["body"],
                title = post["title"]
                )
                serializer = PostSerializer(create_post, many=False)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "PUT":
        try:
            post = Post.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializerUpdate(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "DELETE":
        try:
            post = Post.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    return Response(serializer.data)

@api_view(["GET"])
def posts_user(request,pk):
    
    posts = Post.objects.filter(user_id = pk)
    if posts.exists():
        pass
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(posts, many=True)

    
    return Response(serializer.data)
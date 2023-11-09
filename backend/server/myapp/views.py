from django.http import HttpResponse, Http404, JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, CreatePostSerializer, CrashPadPostSerializer, CreateCrashPadPostSerializer
from .models import Post, CrashPadPost
from .authapp.models import Profile
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import BasePermission


# class PostUserWritePermission(BasePermission):
#     message = "Editing posts is restricted to the author only."

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.author == request.user

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer


class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['author_id'] = 1

        posts_serializer = CreatePostSerializer(data=data)
        print("POSTS SERIALIZER:", posts_serializer)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CrashPadPostView(generics.ListAPIView):
    queryset = CrashPadPost.objects.all()
    serializer_class = CrashPadPostSerializer


class CreateCrashPadPost(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['author_id'] = 1

        posts_serializer = CreateCrashPadPostSerializer(data=data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(generics.RetrieveAPIView):
    def profile(reuqest, pk, username):
            if request.user.is_authenticated:
                user = Profile.objects.get(user_id=pk)
                posts = Post.objects.filter(author=pk).order_by("-created_at")

class ProfilePage(generics.RetrieveUpdateDestroyAPIView):
    pass




# def profile(request, pk):
#     if request.user.is_authenticated:
#         profile = Profile.objects.get(user_id=pk)
#         return Response(profile)

# def post_detail_view(request, post_id, *args, **kwargs):
#     data = {
#         "id": post_id
#     }
#     status = -1
#     try :
#         obj = Post.objects.get(id=post_id)
#         data['caption'] = obj.caption
#         status = 200
#     except:
#         data['message'] = "Not Found"
#         status = 404
#     return JsonResponse(data,status=status)


# class CreatePostSerializer(APIView):
    # serializer_class = CreatePostSerializer

    # def post(request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         caption = serializer.data.get('caption')
    #         image = serializer.data.get('image')
    #         new_post = Post(caption=caption, image=image)
    #         new_post.save()

    #         return Response(PostSerializer(new_post).data, status=status.HTTP_200_OK)

    # the error i got with this code : post() takes 1 positional argument but 2 were given


    # queryset = Post.objects.all()
    # serializer_class = PostSerializer


# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# def add_post_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         new_post = Post(caption=data['caption'])
#         new_post.save()
        

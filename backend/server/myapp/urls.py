from django.urls import path
from .views import PostListView, CreatePost, PostDetailAPIView, PostView, CrashPadPostView
# ProfileView, ProfilePage

urlpatterns = [
    path('posts/<int:pk>', PostDetailAPIView.as_view()),
    path('feed', PostListView.as_view()),
    path('create', CreatePost.as_view()),
    path('posts', PostView.as_view()),
    path('crashpads', CrashPadPostView.as_view())
    # path('/<int:pk>/<str:username>', ProfileView.as_view()),
    # path('<str:username>', ProfilePage.as_view())
    # path('profile/<int:pk>', profile_card),
]


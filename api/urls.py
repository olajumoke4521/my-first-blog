from django.urls import path
from .views import PostList, PostDetail, CommentList, CommentDetail
from api import views
urlpatterns = [
    path('api/', views.PostList),
    path('api/<int:pk>/', views.PostDetail),
    path('', CommentList.as_view()),
    path('', CommentDetail.as_view()),
]

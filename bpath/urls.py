from django.urls import path
from .views import CustomLoginView, RespiteCreate, RespiteList, RespiteDetail, RespiteUpdate, DeleteView, CustomLoginView, DashboardList, RegisterPage
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', DashboardList.as_view(), name='dash'),
    path('respite/', RespiteList.as_view(), name='respites'),
    path('respite/<int:pk>/', RespiteDetail.as_view(), name='respite'),
    path('respite-create/', RespiteCreate.as_view(), name='respite-create'),
    path('respite-update/<int:pk>/', RespiteUpdate.as_view(), name='respite-update'),
    path('respite-delete/<int:pk>/', DeleteView.as_view(), name='respite-delete'),
# --------------------------------------------------------------------------------------------
    path('post/', views.postOverview, name="post-overview"),
    path('post-list/', views.postList, name="post-list"),
    path('post-detail/<str:pk>/', views.postDetail, name="post-detail"),
    path('post-create/', views.postCreate, name="post-create"),
    path('post-update/<str:pk>/', views.postUpdate, name='post-update'),
    path('post-delete/<str:pk>/', views.postDelete, name='post-delete'),
# -------------------------------------------------------------------------------------------  
    path('comment/', views.commentOverview, name="comment-overview"),
    path('comment-list/', views.commentList, name="comment-list"),
    path('comment-detail/<str:pk>/', views.commentDetail, name="comment-detail"),
    path('comment-create/', views.commentCreate, name="comment-create"),
    path('comment-update/<str:pk>/', views.commentUpdate, name='comment-update'),
    path('comment-delete/<str:pk>/', views.commentDelete, name='comment-delete'),
]
from django.urls import path
from .views import CustomLoginView, RespiteCreate, RespiteList, RespiteDetail, RespiteUpdate, DeleteView, CustomLoginView, DashboardList, RegisterPage
from django.contrib.auth.views import LogoutView

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
    
]
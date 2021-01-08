from django.urls import path
from account import views
from django.conf.urls import url, include

urlpatterns = [
    path('accounts/', views.account_list),
    path('accounts/<int:pk>/', views.account),
    path('login/', views.login),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
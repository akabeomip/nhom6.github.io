from django.urls import path
from nguoidung import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('home/', views.userhomepage_view, name='userhome'),
    path('dang_ky/', views.dangky, name='dangky'),
    path('dang_nhap/', auth_views.LoginView.as_view(template_name="LoginPage.html"), name='dangnhap'),
    path('termofservice/', views.termofservice_view, name='termofservice'),
    path('dang_xuat/', views.dangxuat, name='dangxuat'),
    #
    #path('testinbox/', views.phongchat, name='testinbox'),
    path('<str:room_name>/', views.phongchatchinh, name='testchatroom'),
    path('home/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room_name>/', views.getMessages, name='getMessages'),
]
urlpatterns += staticfiles_urlpatterns()
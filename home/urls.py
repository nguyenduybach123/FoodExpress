from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:typeID>', views.menu, name='menu'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Sửa đường dẫn và import tên hàm
    path('view_cart/', views.view_cart, name='view_cart')  # Đảm bảo rằng hàm view_cart cũng được import từ views
]

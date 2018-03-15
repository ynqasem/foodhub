"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static 
from  api.views import RestaurantListAPIView, RestaurantDetailAPIView, RestaurantDeleteAPIView, RestaurantCreateAPIView, RestaurantUpdateAPIView, ItemCreateAPIView, UserRegisterView, LoginAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants_list/', views.list, name="restaurants_list"),
    path('restaurant_detail/<int:restaurant_id>/', views.detail, name="restaurant_detail"),
    path('restaurant_create/', views.create, name="restaurant_create"),
    path('update/<int:restaurant_id>/', views.update, name="restaurant_update"),
    path('delete/<int:restaurant_id>/', views.delete, name='restaurant_delete'),
    path('restaurant_register/', views.user_register, name="register"),
    path('restaurant_login/', views.user_login, name="login"),
    path('restaurant_logout/', views.user_logout, name="logout"),
    path('item/create/<int:restaurant_id>/', views.create_item, name="create_item"),
    path('favorite/<int:restaurant_id>/', views.favorite, name='favorite'),
    path('list/', RestaurantListAPIView.as_view(), name="list"),
    path('detail/<int:restaurant_id>/', RestaurantDetailAPIView.as_view(), name="detail"),
    path('deleteapi/<int:restaurant_id>/', RestaurantDeleteAPIView.as_view(), name="deleteapi"),
    path('create/', RestaurantCreateAPIView.as_view(), name="create"),
    path('updateapi/<int:restaurant_id>/', RestaurantUpdateAPIView.as_view(), name="updateapi"),
    path('item/createapi/<int:restaurant_id>/', ItemCreateAPIView.as_view(), name="itemcreateapi"),
    path('api/register/', UserRegisterView.as_view(), name="api-register"),
    path('api/login/', LoginAPIView.as_view(), name="api-login"),


    ]


    # path('burgermenu_list_page/', views.burger_menu_list),

    
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# you choose whatever url you want. views."the_function_defined_in_the views_file"
# you import the views file from the app
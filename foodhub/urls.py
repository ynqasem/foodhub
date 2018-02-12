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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants_list/', views.list, name="restaurants_list"),
    path('restaurant_detail/<int:restaurant_id>/', views.detail, name="restaurant_detail"),


    # path('burgermenu_list_page/', views.burger_menu_list),

    
]

# you choose whatever url you want. views."the_function_defined_in_the views_file"
# you import the views file from the app
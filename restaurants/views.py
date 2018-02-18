from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import RestaurantForm
from django.shortcuts import get_object_or_404


def list(request):
	context = {
	"restaurants": Restaurant.objects.all(),

	}
	return render(request, 'restaurants_list.html', context)


	# calls the html file detailview.html


def detail(request, restaurant_id):
	context = {
	"restaurant_detail": Restaurant.objects.get(id=restaurant_id),

	}


	return render(request, 'restaurant_detail.html', context)


def create(request):
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("restaurants_list")
	context = {
	"create_form":form,
	}

	return render(request, 'restaurant_create.html', context)


def update(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)
	form = RestaurantForm(instance=restaurant_obj)
	if request.method == "POST":
		form = RestaurantForm(request.POST, instance = restaurant_obj)
		if form.is_valid():
			form.save()
			return redirect("restaurant_detail", restaurant_id=restaurant_obj.id)
	context = {
	"restaurant_obj":restaurant_obj,
	"update_form":form,

	}
	return render(request, 'restaurant_update.html', context)


def delete(request, restaurant_id):
	
	instance = get_object_or_404(Restaurant, id=restaurant_id)
	instance.delete()
	# messages.success(request, "Successfully Deleted!")
	return redirect("restaurants_list")





		# meals_dictionary = {
	# 	"meals": [
	# 	  {
	# 		 "title": "Swiss Cheese Burger",
	# 		 "content": "Description, ingredients, sauces, vegetables, calories",
	# 		 "created": "2018-02-05",
	# 		 "updated": "2018-02-06",
	# 	   },
	# 	   {
	# 		 "title": "Classic Cheese Burger",
	# 		 "content": "Description, ingredients, sauces, vegetables, calories",
	# 		 "created": "2018-02-02",
	# 		 "updated": "2018-02-04",
	# 	   },
	# 	   {
	# 		 "title": "Barbecue Burger",
	# 		 "content": "Description, ingredients, sauces, vegetables, calories",
	# 		 "created": "2018-02-06",
	# 		 "updated": "2018-02-09",
	# 	   },
	# 	   {
	# 		 "title": "Special Burger",
	# 		 "content": "Description, ingredients, sauces, vegetables, calories",
	# 		 "created": "2018-02-01",
	# 		 "updated": "2018-02-01",
	# 	   }
	# ]
	# }
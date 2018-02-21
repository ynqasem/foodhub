from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import RestaurantForm, UserRegisterForm, LoginForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout

def user_login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("restaurants_list")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)

def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			person = form.save(commit=False)
			person.set_password(person.password)
			person.save()
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			login(request, person)
			return redirect("restaurants_list")
	context = {
		"form": form
	}
	return render(request, 'register.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')


def list(request):
	object_list = Restaurant.objects.all()
	object_list = object_list.order_by('publish_date', 'name')
	query = request.GET.get('q')
	if query:
		object_list = object_list.filter(name__contains=query)
	context = {
	"restaurants": object_list,

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
		form = RestaurantForm(request.POST, request.FILES or None)
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
		form = RestaurantForm(request.POST, request.FILES or None, instance = restaurant_obj,)
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
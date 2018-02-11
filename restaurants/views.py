from django.shortcuts import render
from django.http import HttpResponse

def burger_menu(request):
	context = {
	"title": "Burger place",
	"content": "So this area contains the a list of all of the food served in the restuarant",
	"created": "2018-02-08",
	"updated": "2018-02-08",

	}
	return render(request, 'detailview.html', context)


	# calls the html file detailview.html


def burger_menu_list(request):
	meals_dictionary = {
		"meals": [
		  {
			 "title": "Swiss Cheese Burger",
			 "content": "Description, ingredients, sauces, vegetables, calories",
			 "created": "2018-02-05",
			 "updated": "2018-02-06",
		   },
		   {
			 "title": "Classic Cheese Burger",
			 "content": "Description, ingredients, sauces, vegetables, calories",
			 "created": "2018-02-02",
			 "updated": "2018-02-04",
		   },
		   {
			 "title": "Barbecue Burger",
			 "content": "Description, ingredients, sauces, vegetables, calories",
			 "created": "2018-02-06",
			 "updated": "2018-02-09",
		   },
		   {
			 "title": "Special Burger",
			 "content": "Description, ingredients, sauces, vegetables, calories",
			 "created": "2018-02-01",
			 "updated": "2018-02-01",
		   }
	]
	}
	return render(request, 'burgermenu_list.html', meals_dictionary)
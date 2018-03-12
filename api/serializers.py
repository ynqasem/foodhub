from rest_framework import serializers
from restaurants.models import Restaurant 

class RestaurantListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['id', 'name', 'owner' ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = '__all__'

class RestaurantCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name', 'description', 'image']


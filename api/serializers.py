from rest_framework import serializers
from restaurants.models import Restaurant 
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']

class RestaurantListSerializer(serializers.ModelSerializer):
	detail_page = serializers.HyperlinkedIdentityField(
		view_name = 'detail',
		lookup_field = 'id',
		lookup_url_kwarg = 'restaurant_id'
		)
	# owner = serializers.SerializerMethodField()
	owner = UserSerializer()

	class Meta:
		model = Restaurant
		fields = ['id', 'name', 'owner', 'detail_page' ]

	# def get_owner(self, obj):
	# 	return obj.owner.username


class RestaurantDetailSerializer(serializers.ModelSerializer):
	delete_page = serializers.HyperlinkedIdentityField(
		view_name = 'deleteapi',
		lookup_field = 'id',
		lookup_url_kwarg = 'restaurant_id',
		)

	update_page = serializers.HyperlinkedIdentityField(
		view_name = 'updateapi',
		lookup_field = 'id',
		lookup_url_kwarg = 'restaurant_id',
		)

	# owner = serializers.SerializerMethodField()
	owner = UserSerializer()

	class Meta:
		model = Restaurant
		fields = '__all__'

	def get_owner(self, obj):
		return obj.owner.username


class RestaurantCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name', 'description', 'image']


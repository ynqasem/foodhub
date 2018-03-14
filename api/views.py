from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from restaurants.models import Restaurant, Rfavorite, Item 

from .serializers import ( RestaurantListSerializer, 
	RestaurantDetailSerializer,
	RestaurantCreateSerializer, 
	FavoriteCreateSerializer, 
	ItemCreateSerializer, 
	ItemListSerializer,
	RegisterUserSerializer
	)

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrStaff
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User

class UserRegisterView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegisterUserSerializer
	permission_classes = [AllowAny]

class RestaurantListAPIView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	permission_classes = [AllowAny,]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name', 'description', 'owner__username']
	# def get_queryset(self):
	# 	keyword = self.request.query_params.get('ordering', '')
	# 	queryset = Restaurant.objects.filter(name__iexact=keyword)
	# 	return queryset

class RestaurantDetailAPIView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'
	permission_classes = [AllowAny,]


class RestaurantDeleteAPIView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'
	permission_classes = [IsAuthenticated, IsOwnerOrStaff]

class RestaurantCreateAPIView(CreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateSerializer
	permission_classes = [IsAuthenticated,]

	def perform_create(self, serializer):
			#assign the owner
			serializer.save(owner=self.request.user)

class RestaurantUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'
	permission_classes = [IsAuthenticated,IsOwnerOrStaff,] 

class FavoriteView(CreateAPIView):
	queryset = Rfavorite.objects.all()
	serializer_class = FavoriteCreateSerializer
	permission_classes = [IsAuthenticated,]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class ItemCreateAPIView(CreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemCreateSerializer
	permission_classes = [IsAuthenticated,]

	# def perform_create(self, serializer):
	# 		#assign the owner
	# 		serializer.save(owner=self.request.user)

class ItemListAPIView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	permission_classes = [AllowAny,]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name', 'description', 'owner__username']
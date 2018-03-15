from rest_framework import serializers
from restaurants.models import Restaurant, Rfavorite, Item, Ifavorite
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(style={'input_type':'password'}, write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)

	def validate(self, data):
		my_username = data.get('username')
		my_password = data.get('password')

		if my_username == '':
			raise serializers.ValidationError("A username is required to login.")


		# user = User.objects.filter(username=my_username)
		# if user_obj.exists():
		# 	user_obj = user.first()
		# else:
		# 	raise serializers.ValidationError("This username does not exist.")

		try:
			user_obj = User.objects.get(username=my_username)
		except:
			raise serializers.ValidationError("This username does not exist.")

		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination!")

		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)

		data['token'] = token

		return data







class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']

class ItemCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ['name', 'description', 'price', 'restaurant']

class ItemListSerializer(serializers.ModelSerializer):
	# user = UserSerializer()

	class Meta:
		model = Item 
		fields = ['name', 'description', 'price']

class FavoriteCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rfavorite
		fields = ['restaurant']

class FavoriteListSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Rfavorite 
		fields = ['user']

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
	favorites = serializers.SerializerMethodField()
	items = serializers.SerializerMethodField()

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
		fields = ['name', 'description', 'image', 'owner', 'delete_page', 'update_page', 'favorites', 'items']

	def get_owner(self, obj):
		return obj.owner.username

	def get_favorites(self, obj):
		favorites = obj.rfavorite_set.all()
		json_favorites = FavoriteListSerializer(favorites, many=True).data
		return json_favorites

	def get_items(self, obj):
		items = obj.item_set.all()
		json_items = ItemListSerializer(items, many=True).data
		return json_items


class RestaurantCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name', 'description', 'image']


class RegisterUserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
	class Meta:
		model = User 
		fields = ['username', 'first_name', 'last_name', 'email', 'password']

	def create(self, validated_data):
		new_user = User(**validated_data)
		new_user.set_password(validated_data['password'])
		new_user.save()
		return validated_data


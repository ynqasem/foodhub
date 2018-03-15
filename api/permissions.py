from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):
	message = "You are not allowed to do this!"
	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.owner == request.user):
			return True 
		else:
			return False 
from rest_framework.permissions import BasePermission

class IsJobOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        # if request.method == 'POST':
        #     return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method =='GET' :
            return True
        return obj.posted_by == request.user


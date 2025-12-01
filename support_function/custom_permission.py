
from rest_framework.permissions import BasePermission, SAFE_METHODS 



class DistrictServiceObjectPermission(BasePermission):
  
    """
    Custom permission to allow:
    - Admin: Full access
    - Seller: Only read 
    - Customer: Read-only access
    
    """
    def has_permission(self, request, view):
        user = request.user

        # Admin can do anything
        if user.role == "Admin":
            return True

        # Staff, Passenger: Only SAFE methods
        if user.role in ["Staff", "Passenger"]:
            return request.method in SAFE_METHODS

        # Default deny
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user 

        print(user.role)
        if user.role in ['Admin']:
            return True
        
       
        elif user.role in ['Passenger','Staff']:
            if request.method in SAFE_METHODS:
                return True
        else:  
            return False

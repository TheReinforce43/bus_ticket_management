
from rest_framework.permissions import BasePermission, SAFE_METHODS 



class DistrictServiceObjectPermission(BasePermission):
  
    """
    Custom permission to allow:
    - Admin: Full access
    - Seller: Only read 
    - Customer: Read-only access
    
    """
    def has_object_permission(self, request, view, obj):
        user = request.user 

        print(user.roles)
        if user.roles in ['Admin']:
            return True
        
       
        elif user.roles in ['Passenger','Staff']:
            if request.method in SAFE_METHODS:
                return True
        else:  
            return False

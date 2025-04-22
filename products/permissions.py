from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    শুধুমাত্র অ্যাডমিন ইউজার Create/Update/Delete করতে পারবে।
    সাধারণ ইউজাররা শুধুমাত্র Read (GET) করতে পারবে।
    """

    def has_permission(self, request, view):
        # যদি GET/HEAD/OPTIONS হয়, তবে সবার জন্য অনুমতি আছে
        if request.method in SAFE_METHODS:
            return True

        # শুধু অ্যাডমিন হলে Write অপারেশন অনুমোদন
        return request.user and request.user.is_staff

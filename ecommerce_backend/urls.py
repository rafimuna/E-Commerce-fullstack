from django.contrib import admin
from django.urls import path, include

# নিচের দুইটা লাইন media file serve করার জন্য
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),  # app এর urls যুক্ত করলে এখানে করবে
]

# মিডিয়া ফাইল সার্ভ করার জন্য দরকার
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

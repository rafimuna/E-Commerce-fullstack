from django.contrib import admin  # Django-এর admin মডিউল ইমপোর্ট করি
from django.utils.html import format_html  # HTML ফরম্যাট করার জন্য ইউটিলিটি
from .models import Product  # আমাদের তৈরি করা Product মডেল ইমপোর্ট করি

# Product মডেলটি admin panel-এ রেজিস্টার করি
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # admin panel-এর list view-তে যেসব ফিল্ড দেখাবে তা নির্ধারণ করি
    list_display = ('name', 'price', 'image_preview', 'created_at')  # পণ্যের নাম, দাম, ছবি প্রিভিউ এবং তৈরি হওয়ার সময় দেখায়

    # শুধু দেখার জন্য কোন কোন ফিল্ড read-only থাকবে (যেমন ছবি)
    readonly_fields = ('image_preview',)

    # custom মেথড: admin panel-এ ছবি দেখানোর জন্য
    def image_preview(self, obj):
        if obj.image:  # যদি প্রোডাক্টের ছবি থাকে
            return format_html('<img src="{}" style="height: 60px;" />', obj.image.url)
        return "(No image)"
    
    image_preview.short_description = 'Image'  # admin column হেডারে 'Image' নামে দেখাবে

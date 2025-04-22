from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # পণ্যের নাম
    description = models.TextField(blank=True)  # পণ্যের বিবরণ
    price = models.DecimalField(max_digits=10, decimal_places=2)  # পণ্যের দাম
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # কখন তৈরি হয়েছে

    def __str__(self):
        return self.name  # মডেল অবজেক্টের রিটার্ন নাম

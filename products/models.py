from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CONDITION_CHOICES = [
        ('completely_new', 'Completely New'),
        ('almost_new', 'Almost New'),
        ('worn_down', 'Worn Down'),
    ]

    PAYMENT_METHODS = [
        ('venmo', 'Venmo'),
        ('zelle', 'Zelle'),
        ('cash', 'Cash'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    product_type = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_free = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, blank=True)
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_claimed = models.BooleanField(default=False)
    claimed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='claimed_posts')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

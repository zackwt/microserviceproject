# Create your models here.
from django.db import models
from django.conf import settings

class MyModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # add more fields as needed

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # You should store hashed passwords
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    shipping_address = models.TextField()
    billing_address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust max_digits as needed
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the auth user model
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at the time of order

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carts')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=30, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"Payment {self.id} - {self.payment_status}"

class Shipping(models.Model):
    shipping_method = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    estimated_delivery_time = models.CharField(max_length=50)

    def __str__(self):
        return self.shipping_method

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # You can set a range if necessary (e.g., validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"
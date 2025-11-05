

# PS C:\Users\parme\OneDrive\Desktop\shoppinglyx-main(1)\shoppinglyx-main\shoppinglyx-main> python manage.py runserver

# AFTER RUN THIS JUST COPY THE URL ON THE BROWSER ALL HTML,CSS JS FILE RUN AND SHOW THE FRONTEND OF APPLICATION

# AFTER THE ABOVE WRITE ADMIN IN THE BROWSER THEN ADMIN PANAL WILL OPEN


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator
STATE_CHOICES = (
    ('Asam', 'Asam'),
    ('U.P', 'U.P'),
    ('Delhi', 'Delhi'),
    ('Bangloru', 'Bangloru'),
    ('MUmbai', 'MUmbai'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name= models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    
    
    def __str__(self):
        return str(self.id)
    
CATAGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
    
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATAGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='productimg')
    
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1);
    
    def __str(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES=(
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

# Create your models here.
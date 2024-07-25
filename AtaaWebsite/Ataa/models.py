from django.db import models


#Doner and homepage Ghadi
#sign in /up عبد العزيز + البروفايل
#items retrive عبدالله
#ايتيم محدد صالح
# اروى كارت اوردر

class Doneer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Donee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# class Cart(models.Model):  # اروى
#     pass
class catagory(models.Model):  # غدي
         name = models.CharField(max_length=255)

     # class cart(models.Model):  # اروى
class items(models.Model):  # Ghadi
         item_id = models.IntegerField(primary_key=True)
         name = models.CharField(max_length=255)
         size = models.CharField(max_length=50)
         availability = models.IntegerField()
         image = models.CharField(max_length=255)
         category = models.ForeignKey(catagory, on_delete=models.CASCADE)
         amount = models.IntegerField()

         def __str__(self):
             return f"{self.name} "

# class Order(models.Model): اروى
#     pass

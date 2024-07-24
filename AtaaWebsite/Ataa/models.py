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

# class Catagory(models.Model):  # صالح
#     pass

# class Cart(models.Model):  # اروى
#     pass

# class Items(models.Model):
#     pass

# class Order(models.Model):
#     pass

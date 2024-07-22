from django.db import models
#Doner and homepage Ghadi
#sign in /up عبد العزيز + البروفايل
#items retrive عبدالله
#ايتيم محدد  صالح
# اروى كارت اوردر


class Doneer(models.Model): #عبد العزيز  الزهراني
   fristname = models.CharField(max_length=100)
   lastname = models.CharField(max_length=100)
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=128)


class Donee(models.Model):  # عبدالله العنزي


class catagory(models.Model):  # صالح


class cart(models.Model):  # اروى


class items(models.Model):

class order(models.Model):
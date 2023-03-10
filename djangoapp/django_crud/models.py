from django.db import models


#create your models here

class User(models.Model):
    user_id = models.AutoField(primary_key=True) 
    user_uname = models.CharField(max_length=255)
    user_email  = models.EmailField(max_length=255, unique=True)
    user_pwd = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





class Cruding(models.Model):
    c_id  = models.AutoField(primary_key=True)
    post = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)




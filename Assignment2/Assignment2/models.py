from django.db import models

class UserModel(models.Model):
     email = models.CharField(max_length = 60, primary_key=True)
     name = models.CharField(max_length = 30)
     surname = models.CharField(max_length = 40)
     salary = models.IntegerField()
     phone = models.CharField(max_length = 20)
     cname = models.CharField(max_length = 50)
     class Meta:
         db_table = "users"

from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(default='', max_length=100) 
    user_email = models.EmailField(default='', max_length=254)
    user_phone = models.CharField(default='', max_length=11)

    def __str__(self):
        return f"Nome: {self.user_name} | E-mail: {self.user_email} | Número: {self.user_phone}"
    
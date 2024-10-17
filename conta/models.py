from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    data_nascimento = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_nascimento']
    
    def __str__(self):
        return f'{self.nome} - {self.email}'
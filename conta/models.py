from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_nascimento']
    
    def __str__(self):
        return f'{self.nome} - {self.email}'
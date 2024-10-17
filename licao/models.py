from django.db import models


class Licao(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo_html = models.TextField()


    def __str__(self):
        return self.titulo
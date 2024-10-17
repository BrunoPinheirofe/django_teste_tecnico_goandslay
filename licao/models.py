from django.db import models


class Licao(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    conteudo_html = models.TextField(null=False, blank=False)
    
    class Meta:
        verbose_name = 'Lição'
        verbose_name_plural = 'Lições'


    def __str__(self):
        return self.titulo
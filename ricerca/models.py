from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Grafo(models.Model):
    title = models.CharField(max_length=200)
    chiave = models.CharField(max_length=200,primary_key=True)
    tipo = models.CharField(max_length=20,default="")
    data_PC = models.CharField(max_length=30,default="")
    data = models.DateTimeField(default=timezone.now)
#    published_date = models.DateTimeField(blank=True, null=True)

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

    def __str__(self):
        return self.title

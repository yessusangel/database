from django.db import models

# Create your models here.
class categoria producto(models.model):
     idcategoria = model.autofield(primary_key=True)
     nombrecategoria = models.CharField(max_length=70) 

     
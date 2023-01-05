from django.db import models

class Koordinat(models.Model):
    nama_cafe = models.CharField(max_length=50)
    koordinat = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_cafe

class Cafe(models.Model):
    nama_cafe = models.CharField(max_length=50)
    alamat = models.TextField(null=True)
    no_tlp = models.CharField(max_length=20)
    img = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nama_cafe

# Create your models here.

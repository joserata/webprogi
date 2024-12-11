from django.db import models

class Definiciones(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()

    class Meta:
        db_table = 'definiciones'
        managed = False

    def __str__(self):
        return self.titulo

class Documentos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    enlace = models.URLField()

    class Meta:
        db_table = 'documentos'
        managed = False

    def __str__(self):
        return self.titulo

class Normatividad(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    enlace = models.URLField()

    class Meta:
        db_table = 'normatividad'
        managed = False

    def __str__(self):
        return self.titulo

class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='eventos/')
    tipo = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'eventos'
        managed = False

    def __str__(self):
        return self.titulo


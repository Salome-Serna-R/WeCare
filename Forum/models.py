from django.db import models
from django.contrib.auth.models import User


class Comentario(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='recetas_images/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Respuesta(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respuestas')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Respuesta de {self.autor.username} en {self.comentario.titulo}'


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} ha marcado como favorito el comentario {self.comentario.titulo}'


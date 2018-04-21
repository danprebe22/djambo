from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    """
    Modelo para almacenar los posg
    """
    autor = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    fechaCreacion = models.DateTimeField(
        default= timezone.now
    )

    fechaPublicacion =models.DateTimeField(
        blank= True,null=True
    )

    def publicar(self):
        """
        MÉTODO PARA OBTENER LA FECHA DE PUBLICACIÓN CUANDO SE PUBLIQUE ALGÚN POST
        """
        self.fechaPublicacion = timezone.now()
        self.save()

#MÉTODO MÁGICO QUE NOS PERMITE CASTEAR UN OBJETO A UNA CARPETA
    def __str__(self):
        return self.titulo
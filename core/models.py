from django.db import models
from stdimage.models import StdImageField


def get_file_path(self, filename):
    return f'media/{self.nome}-{self.raca}'


class Dog(models.Model):
    nome = models.CharField("Nome", max_length=50)
    raca = models.CharField("Raça", max_length=50)
    imagem = StdImageField('Imagem', upload_to=get_file_path, null=True)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

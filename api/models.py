from distutils.command.upload import upload
from django.db import models


## TABELA DE CALIBRE

class CalibreModel(models.Model):
    desc_calibre = models.CharField(
        max_length=45,
        verbose_name='Descrição do calibre',
        unique=True
        )

    def __str__(self):
        return f'{self.desc_calibre}'


## TABELA DE TIPO DE OBJETO
class ObjetoTipoModel(models.Model):
    tipo_de_objeto = models.CharField(
        max_length=64,
        verbose_name='Tipo de objeto',
        unique=True
        )

    def __str__(self):
        return f'{self.tipo_de_objeto}'


## TABELA DE OBJETOS
class ObjetoModel(models.Model):
    objeto_tipo = models.ForeignKey(
        ObjetoTipoModel,
        on_delete=models.CASCADE,
        verbose_name='Objeto tipo'
        )

    def __str__(self):
        return f'{self.objeto_tipo}-{self.id}'


## TABELA DE ARMAS
class ArmaModel(models.Model):

    calibre = models.ForeignKey(
        CalibreModel,
        on_delete=models.CASCADE ,
        verbose_name='Calibre'
        )


    objeto = models.ForeignKey(
        ObjetoModel,
        on_delete=models.CASCADE ,
        verbose_name='Objeto'
        )

    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField(verbose_name='Quantidade de tiros')
    valor_estimado = models.FloatField(verbose_name='Valor estimado')
    imagem = models.ImageField()


    def __str__(self):
        return f'{self.objeto}'

class AmmoModel(models.Model):
    calibre = models.ForeignKey(
        CalibreModel,
        on_delete=models.CASCADE ,
        verbose_name='Calibre'
        )

    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField(verbose_name='Valor estimado')

    objeto = models.ForeignKey(
        ObjetoModel,
        on_delete=models.CASCADE ,
        verbose_name='Objeto'
        )
    def __str__(self):
        return f'{self.objeto}'
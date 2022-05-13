from rest_framework import serializers

from api.models import ArmaModel, CalibreModel, AmmoModel, ObjetoModel, ObjetoTipoModel


class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalibreModel
        fields = '__all__'


class TypeObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetoTipoModel
        fields = '__all__'


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetoModel
        fields = '__all__'




class GunSerializer(serializers.ModelSerializer):
    objeto = ObjetoSerializer(read_only = True)

    def create(self,validated_data):
        tipoArma = ObjetoTipoModel.objects.get(tipo_de_objeto = 'arma')
        objeto = ObjetoModel(objeto_tipo = tipoArma)
        objeto.save()
        
        return ArmaModel.objects.create(objeto=objeto , **validated_data)


    class Meta:
        model = ArmaModel
        fields = '__all__'
        read_only_fields = ['objeto']




class AmmoSerializer(serializers.ModelSerializer):
    objeto = ObjetoSerializer(read_only = True)


    def create(self,validated_data):
        tipoAmmo = ObjetoTipoModel.objects.get(tipo_de_objeto = 'munição')
        objeto = ObjetoModel(objeto_tipo = tipoAmmo)
        objeto.save()
        
        return AmmoModel.objects.create(objeto=objeto , **validated_data)



    class Meta:
        model = AmmoModel
        fields = '__all__'
        read_only_fields = ['objeto']
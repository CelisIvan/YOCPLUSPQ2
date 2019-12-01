from rest_framework import serializers
from .models import *

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('id','url','nombre','costo','descripcion','lugar','siglas','fecha','asistentes')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")
    class Meta:
        model = User
        fields = ('url','username','email', 'first_name', 'last_name', 'password', 'is_superuser')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('id','url','user','age','empresa','estado')

class BoletoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Boleto
        fields = ('user','id','url',UserSerializer,'codigo','evento')

class EstadoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('id','url','nombre')

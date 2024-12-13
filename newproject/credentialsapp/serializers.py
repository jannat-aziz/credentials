from rest_framework import serializers
from .models import Practitioner, Credential

class PractitionerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Practitioner
        fields= '__all__'


class CredentialsSerializer(serializers.HyperlinkedModelSerializer):

    # practitioner_id=serializers.PrimaryKeyRelatedField(
    #     source='practitioner',
    #     queryset=Practitioner.objects.all()
    #     )

    class Meta:
        model = Credential
        fields ='__all__'


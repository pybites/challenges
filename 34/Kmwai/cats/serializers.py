from rest_framework import serializers
from .models import Cats


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cats
        fields = ('name', 'genus', 'species', 'binomial_name', 'created_at', 'updated_at')

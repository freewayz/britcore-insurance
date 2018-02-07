from rest_framework import serializers
from .models import RiskType, RiskFormField, RiskFormFieldOption



class RiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskType
        fields = "__all__"


class RiskFormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFormField
        fields = "__all__"


class RiskFormFieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFormFieldOption
        fields = "__all__"
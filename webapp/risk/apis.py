from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .serializers import (
    RiskTypeSerializer, RiskFormFieldSerializer,
    RiskFormFieldOptionSerializer
)
from .models import (
    RiskType, RiskFormField, RiskFormFieldOption
)

__autho__ = "peter"

class RiskTypeAPI(viewsets.ModelViewSet):
    serializer_class  = RiskTypeSerializer
    queryset = RiskType.objects.all()
    

class FormFieldAPI(viewsets.ModelViewSet):
    serializer_class = RiskFormFieldSerializer
    queryset = RiskFormField.objects.all()


class RiskTypeFormFieldAPI(viewsets.ViewSet):
    def retrieve(self, request, risk_type_pk):
        risk_type = get_object_or_404(RiskType, pk=risk_type_pk)
        form_fields = RiskFormField.objects.filter(risk_type=risk_type)
        serialized_data = RiskFormFieldSerializer(instance=form_fields, many=True)
        return Response(
            data=serialized_data.data, 
            status=HTTP_200_OK
        )



class FormFieldOptionAPI(viewsets.ModelViewSet):
    serializer_class = RiskFormFieldOptionSerializer
    queryset = RiskFormFieldOption.objects.all()
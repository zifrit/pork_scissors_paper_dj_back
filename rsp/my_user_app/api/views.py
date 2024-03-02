from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from . import serializers
from .. import models


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializers
    filterset_fields = [
        'tg_id',
        'username',
    ]

    @action(methods=['post'], detail=False, url_path='check-user')
    def check_user(self, request):
        data = request.data
        user = models.CustomUser.objects.filter(tg_id=data['id']).exists()
        return Response({'status': user})

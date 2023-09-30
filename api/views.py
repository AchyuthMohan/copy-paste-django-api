from rest_framework import generics,mixins,viewsets,status
from .models import (Car)
from .serializers import (CarSerializer)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
# Create your views here.

class CarViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=CarSerializer
    queryset=Car.objects.all()

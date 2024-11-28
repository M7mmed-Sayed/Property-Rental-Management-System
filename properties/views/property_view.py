from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Property
from user.permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters
from ..serializers import PropertySerializer
from ..filters import LocationFilter
from rest_framework.response import Response

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LocationFilter 

    # pass the current location to the serialzer to calc the dis for each property
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)
    

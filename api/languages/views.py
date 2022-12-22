from .serializers import *
from rest_framework import viewsets
from languages.models import *
 
"""(vewset.ModelViewSet): list, create, retrieve, partical_update, destroy"""


class LanguageViewSet(viewsets.ModelViewSet):
  queryset = Language.objects.all()
  serializer_class = LanguageSerializer

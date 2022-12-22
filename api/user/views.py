from .serializers import *
from rest_framework import viewsets
from user.models import *

"""(vewstes.ModelViewSet): list, create, retrieve, partical_update, destroy"""


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializier_class = UserSerializer

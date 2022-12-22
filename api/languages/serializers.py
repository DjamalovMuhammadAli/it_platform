from languages.models import *
from rest_framework import serializers


class LanguageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Language
    fields = "__all__"

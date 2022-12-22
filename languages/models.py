from django.db import models

py = "Python"
django = "Django"
drf = "DjangoRestFramework"
fastapi = "FastAPI"
postgresql = "PostgreSQL"
Languages_choices = (
  (py, "Python"),
  (django, "Django"),
  (drf, "DjangoRestFramework"),
  (fastapi, "FastAPI"),
  (postgresql, "PostgreSQL"),
)


class Language(models.Model):
  Language = models.CharField(max_length=30, choices=Languages_choices, default=None)


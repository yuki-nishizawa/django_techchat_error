from django.db import models
from django.conf import settings


class Question(models.Model):
  class Meta:
    db_table = 'questions'

  title = models.CharField(null=False)
  content = models.TextField(null=False)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

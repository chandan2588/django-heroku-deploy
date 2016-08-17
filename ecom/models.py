from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProdTable(models.Model):
    pname = models.CharField(max_length=200)
    pamount = models.FloatField(default=0)

    def __str__(self):
        return self.pname, self.pamount

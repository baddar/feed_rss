from django.db import models


class Feed(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url
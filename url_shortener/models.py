from django.db import models

from url_shortener.baseconv import base62

class Link(models.Model):
    url = models.URLField(verify_exists=True, unique=True)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def to_base62(self):
        return base62.from_decimal(self.id)

    def __unicode__(self):
        return self.to_base62() + ' : ' + self.url

from django.db import models

class BizInfo(models.Model):
    pblanc_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    region = models.TextField()
    registered_at = models.DateTimeField()
    hashtag = models.TextField()
    iframe_src = models.URLField()
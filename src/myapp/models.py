from django.db import models
from django.utils import timezone

# Create your models here.
class Externaltoken(models.Model):
    id = models.AutoField(primary_key=True)
    api_name = models.CharField(null=False, blank=False, max_length=255)
    token_json = models.JSONField()
    expires_in = models.IntegerField(blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"created_at: {self.created_at}"


class Webhooklog(models.Model):
    id = models.AutoField(primary_key=True)
    log = models.JSONField()
    eventId = models.CharField(max_length=255, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"created_at: {self.created_at}"

# from django.db import models

from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.models import create_api_key
from client.models import Client
from django.db.models import signals
from django.contrib.auth.models import User

# Create your models here.

signals.post_save.connect(create_api_key, sender=User)


class ClientResources(ModelResource):
    class Meta:
        queryset = Client.objects.all()
        resource_name = 'keys'
        fields = ['license_key', 'domain', 'expire']
        allowed_methods = ['get']
        signals.post_save.connect(create_api_key, sender=User)
        authentication = ApiKeyAuthentication()

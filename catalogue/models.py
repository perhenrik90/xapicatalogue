from django.db import models


class LRS(models.Model):

    url = models.TextField(max_length=300)
    local_name = models.TextField(max_length=30)

    username = models.TextField(max_length=100)
    key = models.TextField(max_length=100)


class xResource(models.Model):

    url = models.TextField(max_length=300)
    name = models.TextField(max_length=80)
    description = models.TextField(max_length=400)
    

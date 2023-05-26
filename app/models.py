from django.db import models
from django.core import validators

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(7)])
    def __str__(self):
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField(validators=[validators.RegexValidator('[1-9a-zA-Z]\w*[.]?\w+@gmail[.]com')])
    def __str__(self):
        return self.name
    
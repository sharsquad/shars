from django.db import models


# Create your models here.

class Data(models.Model):
    title = models.CharField('Name', max_length=50)
    description = models.CharField('Description', max_length=250)
    changelog = models.TextField('Changelog')
    datetime = models.DateTimeField('Date/Time')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'

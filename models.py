from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.text


from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=150, null=True)
    sub_title = models.TextField(max_length=250, null=True)
    image = models.ImageField(upload_to='images/', blank=False)

    def __str__(self):
        return self.title

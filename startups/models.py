from django.db import models

class Startup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=500)  # This field is the one missing in the database
    website_url = models.URLField(max_length=500)

    def __str__(self):
        return self.name
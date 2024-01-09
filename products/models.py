from django.db import models


class Category (models.Model):
    name= models.CharField(max_length=270)
    user_friendly_name = models.CharField(max_length=270, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_user_friendly_name(self):
        return self.user_friendly_name
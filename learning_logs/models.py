from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)  # talk about SQL
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


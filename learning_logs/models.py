from django.db import models

class Topic(models.Model):  # singular turns to Plural in admin
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)  # talk about SQL
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Something specific learned about a Topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # show that it needs something set on_delete
    text = models.TextField()  # let's not limit this one
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."  # display a clipped version of the entry


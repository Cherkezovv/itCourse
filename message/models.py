from django.db import models


class Messages(models.Model):
    subject = models.CharField(max_length=200)
    from_email = models.EmailField()
    message = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Message'

    def __str__(self):
        return str(self.id)

from django.db import models


class News(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Habarlar'
        verbose_name = 'Habar'

    def __str__(self):
        return self.text

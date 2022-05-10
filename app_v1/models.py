from django.db import models

# Create your models here.

class Score(models.Model):
    name = models.CharField(max_length=64)
    score = models.IntegerField()
    date_created = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        unique_together = ('name', 'score')
        ordering = ('-score', 'date_created', 'name')

    def __str__(self):
        return f'{self.name} : {self.score}'

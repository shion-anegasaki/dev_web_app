from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField('text', max_length=300)
    is_done = models.BooleanField('is done', default=False)

    class Meta:
        db_table = 'todos'

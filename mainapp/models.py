from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.FloatField()
    published = models.DateField(auto_now_add=True, db_index=True)
    


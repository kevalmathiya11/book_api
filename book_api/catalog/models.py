from django.db import models

class Book(models.Model):
    title  = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='covers/',blank= True,null= True)

    def __str__(self):
        return self.title
    
    
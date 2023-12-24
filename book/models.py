from django.db import models

# Create your models here.
class Auther(models.Model):
    name=models.CharField(max_length=200)
    birth_date=models.DateField()

    def __str__(self):
        return self.name
    
class Books(models.Model):
    auther=models.ForeignKey(Auther,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    published_date=models.DateField()

    def __str__(self):
        return self.title
    
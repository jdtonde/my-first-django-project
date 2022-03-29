from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, SlugField
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption=models.CharField(max_length=25)

    def __str__(self):
        return self.caption
    
  


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()

    def nom_complet(self): 
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.nom_complet()



class Post(models.Model):
    title=models.CharField(max_length=110)
    excerpt=models.CharField(max_length=200)
    imageName=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag=models.ManyToManyField(Tag) 
    
def __str__(self):
    return f"{self.title} {self.excerpt}"





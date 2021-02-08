from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


# category model 

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title 

    
        



# Tag model 
class Tag(models.Model):
    """Model definition for Tag."""
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)

  
    def __str__(self):
        """Unicode representation of Tag."""
        return self.title



    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag,self).save()    



    
    def get_absolute_url(self):
        return reverse("tags", args=[str(self.slug)])
        












# flower model 
class Flower(models.Model):
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    image = models.FileField(upload_to='media/',blank=True)
    slug = models.SlugField(blank=True,default='')
    category = models.ForeignKey(Category, null=True,  on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)






    def __str__(self):
        return self.title


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Flower,self).save()


    def get_absolute_url(self):
        return reverse("detail", args=[str(self.slug)])
    
    


class Movie(models.Model):

    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3

    RATINGS = (

        (NOT_RATED , 'NR - not rated'),
        (RATED_G , 'G - General Audience'),
        (RATED_PG , 'PG - Parential Guidance''Suggested'),
        (RATED_R , 'R - Restricted')

        )

    title = models.CharField(max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS,default=NOT_RATED)
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)


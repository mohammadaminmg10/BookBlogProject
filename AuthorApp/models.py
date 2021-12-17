from django.db import models

# Create your models here.
STATUS = ((0, "DEAD"), (1, "ALIVE"))


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=1)
    content = models.TextField()
    author_image = models.ImageField(upload_to='Author/', default=0)

    def __str__(self):
        return self.name

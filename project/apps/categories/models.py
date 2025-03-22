from django.db import models


class Category(models.Model):
    """
    Model representing a category for photos.
    
    Attributes
    ----------
    name : CharField
        Unique name of the category.

    Notes
    -----
    Category name also resembles name of a directory that stores photos of certain category.
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
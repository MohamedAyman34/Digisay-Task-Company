from django.db import models

# Create your models here.

class Category(models.Model):
    parent_category = models.CharField(("Parent Category"),max_length=50)
    sub_category_1  = models.CharField(("Sub Category 1"),max_length=50 ,blank=True,null=True)
    sub_category_2  = models.CharField(("Sub Category 2"),max_length=50 ,blank=True,null=True)

    def __str__(self):
        return self.parent_category
    
    class Meta:
        verbose_name_plural = 'Categories'
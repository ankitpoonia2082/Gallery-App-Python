from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    
    # use dender method to show the data to admin panel if i used to another way to register in admin.py
    def __str__(self):
        return self.title          
    


class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    uploaded_by =  models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Uploaded_Image/')


    def __str__(self):
        return f'{self.title} \t{self.desc} \t{self.uploaded_by}\t{self.uploaded_at}\t{self.cat}\t{self.image}'
        
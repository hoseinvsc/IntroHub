from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیحات")
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
    
    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product,on_delete=models.PROTECT)

    def __str__(self):
        return f'image of {self.product.name} {self.id}'

class Category(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self):
        return self.title
    
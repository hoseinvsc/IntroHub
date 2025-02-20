from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیحات")
    
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
    
    def __str__(self):
        return self.name
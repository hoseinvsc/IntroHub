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

    @property
    def get_first_image(self):
        images_list = self.product_images.all()
        if images_list.exists():
            
            return images_list.first().image.url    
        return None


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images',help_text='image size must be 1024*614 pixel')
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name='product_images')

    def __str__(self):
        return f'image of {self.product.name} {self.id}'

class Category(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self):
        return self.title
    





class Customer(models.Model):
    CUSTOMER_TYPES = [('i', 'شخص'),('company', 'شرکت/سازمان')]
    name = models.CharField( max_length=200, verbose_name="نام شخص/سازمان")
    customer_type = models.CharField( max_length=20, choices=CUSTOMER_TYPES, default='i',verbose_name="نوع مشتری")
    phone = models.CharField( max_length=11, verbose_name="شماره تماس")
    address = models.TextField(verbose_name="آدرس")
    image = models.ImageField(upload_to='images/customer', null = True ,help_text= 'image size must be 142 * 41')
    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"
    
    def __str__(self):
        return self.name
    


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    summary = models.TextField(verbose_name="خلاصه")
    description = models.TextField(verbose_name="شرح", default='No description')  # مقدار پیش‌فرض
    cover = models.ImageField(upload_to='images/', verbose_name="عکس کاور", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیرفعال")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

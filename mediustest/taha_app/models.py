from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = ("Products")
        
    def __str__(self):
        return str(self.title)
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    file_path = models.URLField()
    
    class Meta:
        verbose_name_plural = ("Product Images")
        
    def __str__(self):
        return str(self.file_path)

    
class Variant(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = ("Variants")
        
    def __str__(self):
        return str(self.title)
    
    
class ProductVariant(models.Model):
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = ("Product Variants")
        
    def __str__(self):
        return str(self.variant_title)
    
    
class ProductVariantPrice(models.Model):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name_plural = ("Product Variants Prices")
        
    def __str__(self):
        return str(self.price)
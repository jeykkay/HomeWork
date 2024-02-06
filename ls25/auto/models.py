from django.db import models


class Auto(models.Model):
    status = models.BooleanField(default=False)
    vin_num = models.CharField(max_length=255)
    model = models.ForeignKey('ModelAuto', on_delete=models.CASCADE)
    auto_user = models.ForeignKey('UserAuto', on_delete=models.CASCADE)
    brand = models.ForeignKey('BrandAuto', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vin_num} - {self.brand}'


class ModelAuto(models.Model):
    name = models.CharField(max_length=255)
    name_brand_auto = models.ForeignKey('BrandAuto', on_delete=models.CASCADE)


class BrandAuto(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='auto_logo/images/', blank=True)


class UserAuto(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True)

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    tel = PhoneNumberField()
    hon = models.IntegerField(verbose_name='Precios de Honorarios')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['name']

    def __str__(self):
        return self.name
    

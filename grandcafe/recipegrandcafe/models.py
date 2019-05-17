from django.db import models

# Create your models here.


image = models.ImageField(blank=True, upload_to='images/blog/%Y/%m/%d', help_text='150x150px', verbose_name='Ссылка картинки')

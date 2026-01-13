from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE= {
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    }
    name= models.CharField(max_length= 1000)
    image= models.ImageField(upload_to='chais/')
    date_added= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    type= models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default='PL')
    description= models.TextField(default='')

    def __str__(self):
        return self.name


# One to Many Relationship
class ChaiReview(models.Model):
    chai= models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.IntegerField()
    comment= models.TextField()
    date_added= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name} - Rating: {self.rating}"
    
# Many to Many Relationship
class Store(models.Model):
    name= models.CharField(max_length=200)
    location= models.CharField(max_length=300)
    chai_varieties= models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name
    
# One to One Relationship
class ChaiCertificate(models.Model):
    chai= models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number= models.CharField(max_length=100)
    issue_date= models.DateField(default=timezone.now)
    valid_until= models.DateField()

    def __str__(self):
        return f"Certificate {self.certificate_number} for {self.chai.name}"
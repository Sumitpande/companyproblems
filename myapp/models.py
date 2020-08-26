from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError

def validate_image(image):
    file_size = image.file.size
#    limit_kb = 150
#    if file_size > limit_kb * 1024:
#        raise ValidationError("Max size of file is %s KB" % limit)

    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)

class User(AbstractUser):
    pass

class Company(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    c_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.c_name}"

   
 
    
class Problems(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    c_name = models.ForeignKey(
        "Company", on_delete=models.CASCADE)
    problem = models.CharField(max_length=255)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    image = models.FileField(upload_to='images/',validators=[validate_image,FileExtensionValidator(allowed_extensions=['jpeg','jpg','pdf'])], blank=True, null=True, editable=True)
    
    video_url = models.URLField(max_length=200)
    
    def __str__(self):
        return f"{self.problem}"

    
class Student(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    s_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    branch = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.s_name}"  
    

class Solution(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    s_name = models.ForeignKey(
        "Student", on_delete=models.CASCADE)
    problem = models.ForeignKey(
        "Problems", on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    

    
    
class Solution_progress(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    s_name = models.ForeignKey(
        "Student", on_delete=models.CASCADE)
    progress = models.CharField(max_length=255,null=True)
    progress_details = models.CharField(max_length=255,null=True)
    date = models.DateTimeField()
    image = models.FileField(upload_to='images/',validators=[validate_image,FileExtensionValidator(allowed_extensions=['jpeg','jpg','pdf'])], blank=True, null=True, editable=True)
    video_url = models.URLField(max_length=200)
    
    

  


from django.db import models


# Create your models here.

class Student_records(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20)
    guardian_name = models.CharField(max_length=40,null=False)
    guardian_mobile_no = models.CharField(null=False)
    student_photo = models.ImageField()
    student_aadhaar_number = models.CharField(null=False)
    guardian_aadhaar_number = models.CharField(null=False)
    permanent_address = models.CharField(null=False)
    udisse_code = models.CharField()
    admission_class = models.CharField(null=False)
    previous_school = models.CharField()
    current_address = models.CharField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class NewUserRegistration(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(default=f"{first_name}!@#")
    mobile_no = models.CharField(default="xxxxx-xxxx")
    email = models.EmailField(default="abc@gmail.com")
    profile_photo = models.ImageField()
    address = models.CharField()
    password = models.CharField()
    creates_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

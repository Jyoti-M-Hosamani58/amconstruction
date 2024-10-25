from django.db import models

# Create your models here.



class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype=models.CharField(max_length=50)

class Service_image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"



class Residential(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Building(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Struturaldesign(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Elevation(models.Model):
    image = models.ImageField(upload_to='elevations/')  # This field must exist
    description = models.TextField()

    def __str__(self):
        return self.description


class Renovation(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Swimming(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Freelancing(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Joinventure(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Landscape(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Fabrication(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Paintcontract(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Retro(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Detailed(models.Model):
    image = models.ImageField(upload_to='uploads/')
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Completed_project(models.Model):
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')

class Ongoing_project(models.Model):
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')

class Dop(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Certificate(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Listofmachine(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"
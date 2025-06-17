from django.db import models

class Hero (models.Model):
    # portfolio_holder = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, default='Name')
    last_name = models.CharField(max_length=255, default='Surname')
    direction = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HeroCarusel (models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class HeroImage (models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hero_images/')

    def __str__(self):
        return str(self.image.name)
    
class About (models.Model):
    image = models.ImageField(upload_to='about_images/')
    introduction = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    facebook = models.URLField(null=True)
    twitter = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    def __str__(self):
        return str(self.email)
    
class Service (models.Model):
    desc = models.TextField()
    image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return str(self.desc)

class ServiceHighlight (models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    desc = models.TextField()

    def __str__(self):
        return str(self.desc)
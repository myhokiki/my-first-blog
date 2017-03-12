from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField("This is Sample Text")
    created_date = models.DateTimeField (default = timezone.now)
    published_date = models.DateTimeField (blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Pet(models.Model):
    cat = 'cat'
    kitten = 'kitten'
    dog = 'dog'
    puppy = 'puppy'

    PET_CHOICES = (
        (cat, 'Cat'),
        (kitten, 'Kitten'),
        (dog, 'Dog'),
        (puppy, 'Puppy'),
    )
    pet_choice=models.CharField(max_length=10,
                                choices = PET_CHOICES,
                                default = dog)
    def is_chosen(self):
        return self.pet_choice in (self.cat,self,puppy)

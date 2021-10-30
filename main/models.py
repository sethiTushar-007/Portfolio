from django.db import models
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Custom Validations


def validate_divisibility_by_five(value):
    if value % 5 != 0:
        raise ValidationError(
            ('%(value)s is not divisible by 5'),
            params={'value': value},
        )

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=500)
    avatar = models.URLField(max_length=1000)
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=10)
    birth_date = models.DateField()
    description = models.TextField()
    resume = models.URLField(
        max_length=1000, default=None, blank=True, null=True)


class JobTitle(models.Model):
    order = models.PositiveSmallIntegerField(unique=True)
    code = models.CharField(max_length=2, unique=True)
    title = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']


class Skill(models.Model):
    order = models.PositiveSmallIntegerField(unique=True)
    code = models.CharField(max_length=2, unique=True)
    title = models.CharField(max_length=500)
    percent = models.PositiveSmallIntegerField(validators=[
                                               validate_divisibility_by_five, MinValueValidator(5), MaxValueValidator(100)])
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']


class SocialIcon(models.Model):
    order = models.PositiveSmallIntegerField(unique=True)
    code = models.CharField(max_length=2, unique=True)
    fontawesome_icon = models.CharField(max_length=500)
    url = models.URLField(max_length=1000)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

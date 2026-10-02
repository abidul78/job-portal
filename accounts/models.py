from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('employer', 'Employer'),
        ('seeker', 'Job Seeker'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='seeker'
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    skills = models.CharField(
        max_length=300,
        blank=True
    )

    education = models.TextField(
        blank=True
    )

    experience = models.TextField(
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )
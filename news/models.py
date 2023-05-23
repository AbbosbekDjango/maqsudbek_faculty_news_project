from django.urls import reverse
from django.utils import timezone

from django.db import models

# from .managers import PublishedManager

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
    name = models.CharField(verbose_name="Kategoriya", max_length=150)

    def __str__(self):
        return self.name

class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    title = models.CharField(verbose_name="Sarlavha", max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(verbose_name="Rasm", upload_to="news/images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(verbose_name="Yuklagan vaqti", default=timezone.now)
    created_time = models.DateTimeField(verbose_name="Yaratilgan vati", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="Tahrirlangan vaqti", auto_now=True)
    status = models.CharField(verbose_name="Holati", max_length=2, choices=Status.choices,
                              default=Status.Draft
                              )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])


class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(verbose_name='Ism', max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=150)

    def __str__(self):
        return self.name

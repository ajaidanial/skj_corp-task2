from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class BaseAppModel(models.Model):
    """Base model to hold the utility data."""

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(BaseAppModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(BaseAppModel):
    """Comment's model."""

    pass


class Post(BaseAppModel):
    """Post's model."""

    comments = models.ManyToManyField(to=Comment, related_name="post", blank=True)

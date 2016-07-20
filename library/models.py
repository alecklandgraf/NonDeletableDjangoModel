"""Library models."""
from __future__ import unicode_literals

from django.db import models


class ActiveOnly(models.Manager):
    """Manager to filter out inactive results."""

    use_for_related_fields = True

    def get_queryset(self):
        """Overwrite the default django queryset."""
        return super(ActiveOnly, self).get_queryset().filter(active=True)


class Author(models.Model):
    """Authors of books."""

    name = models.TextField()


class Book(models.Model):
    """A book you can read, with an author."""

    active = models.BooleanField()
    author = models.ForeignKey(Author, related_name="books")
    title = models.TextField()
    objects = ActiveOnly()
    # try adding the following...
    default_manager = ActiveOnly()
    inactive_objects = models.Manager()

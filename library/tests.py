"""The tests for the Stack Overflow issue."""
from django.test import TestCase
from library.models import Author, Book


class RelativeLookupQueryTests(TestCase):
    """Test for the Stack Overflow issue."""

    def test_inner_join_doesnt_exclude_inactive_books(self):
        """The tests the inner join where clause isn't set by the custom model manager's get_queryset."""
        bill = Author.objects.create(name="Bill")
        Book.objects.create(title="Hamlet", author=bill, active=False)

        self.assertEquals(
            Book.objects.count(),
            0,
            'Should have zero results since active=False is excluded in the queryset')
        self.assertEquals(
            Author.objects.filter(books__title="Hamlet").first(),
            None,
            'Since the book is inactive, we should not get the related results.')

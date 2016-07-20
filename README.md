To answer the Stack Overflow question http://stackoverflow.com/questions/38470569/django-override-behavior-of-double-underscore-relationship-lookup-in-queries/38491133#38491133


License MIT

### Quick Start
From within a virtualenv:

```console
pip install -r requirements.txt
python manage.py migrate
```

### strange relations
Even though the `Book`'s default queryset has been filtered to include books with `active=True`, when we query from a related Django Model we are able to get results back with `active=False`.

```pycon
>>> from library.models import Author, Book
>>> bill = Author.objects.create(name="Bill")
>>> hamlet = Book.objects.create(title="Hamlet", author=bill, active=False)
>>> Book.objects.count()
0
>>> Author.objects.filter(books__title="Hamlet").first().name
u'Bill'
```

We expect the `Book.objects.count()` to be 0 because the only book has `active=False`, but are then able to find the author of the inactive book.

How can we prevent that?

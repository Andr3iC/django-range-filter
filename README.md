django-range-filter 
=======================
A quick but imperfect implementation of range filter in django admin.


Acknowledgements
----------------
The initial version is adapted from djaong-datefilterspec written by Tomas Zulberti, see https://github.com/tzulberti/django-datefilterspec

Installation
------------

Add range_filter to settings.INSTALLED_APP:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'range_filter'
    )

After this, if you have a model like this one:

.. code-block:: python

    class MyModel(models.Model):
        ...
        score = models.DecimalField()
        created = models.DateField()
        

To allow to filter the fields by range, you must edit the corresponding admin.ModelAdmin like this:

.. code-block:: python

    from daterange_filter.filter import DateRangeFilter, DecimalRnageFilter
    from django.contrib import admin
    from models import MyModel

    class MyModelAdmin(admin.ModelAdmin):
        list_filter = (
            ('score', DecimalRangeFilter),
            ('created', DateRangeFilter),
            ...
        )

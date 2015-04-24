=======================================
Django bootstrap forms for django-jinja
=======================================

Port of [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) which is compatible with 
[django-jinja](https://github.com/niwibe/django-jinja).

Twitter Bootstrap for Django Forms.

See [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) for documentation. Usage should
be the except except:
* there's no need to `{% load bootstrap %}`  as template tags are preloaded in django-jinja.
* add `bootstrapform_jinja` to `INSTALLED_APPS` not `bootstrapform`.

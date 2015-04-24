=======================================
Django bootstrap forms for django-jinja
=======================================

[![Build Status](https://travis-ci.org/samuelcolvin/django-jinja-bootstrap-form.svg?branch=master)](https://travis-ci.org/samuelcolvin/django-jinja-bootstrap-form)

Port of [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) which is compatible with 
[django-jinja](https://github.com/niwibe/django-jinja).

Twitter Bootstrap for Django Forms.

See [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) for documentation. Usage should
be the same except:
* there's no need to `{% load bootstrap %}`  as template tags are preloaded in django-jinja.
* add `bootstrapform_jinja` to `INSTALLED_APPS` not `bootstrapform`.

=======================================
Django bootstrap forms for django-jinja
=======================================

[![Build Status](https://travis-ci.org/samuelcolvin/django-jinja-bootstrap-form.svg?branch=master&style=flat)](https://travis-ci.org/samuelcolvin/django-jinja-bootstrap-form)
[![PyPI Status](https://img.shields.io/pypi/v/django-jinja-bootstrap-form.svg?style=flat)](https://pypi.python.org/pypi/django-jinja-bootstrap-form)

Port of [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) which is compatible with 
[django-jinja](https://github.com/niwibe/django-jinja).

Twitter Bootstrap for Django Forms.

**django-jinja-bootstrap-form** has been used in production for 6 months and is stable.

Supports Django 1.7, 1.8. Python 2.7, >=3.3.

See [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) for documentation. Usage should
be the same except:
* there's no need to `{% load bootstrap %}`  as template tags are preloaded in django-jinja.
* add `bootstrapform_jinja` to `INSTALLED_APPS` not `bootstrapform`.

### To Install

    pip install django-jinja-bootstrap-form

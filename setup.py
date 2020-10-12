from setuptools import setup, find_packages
from bootstrapform_jinja.meta import VERSION

description = """
django-jinja-bootstrap-form
===========================

`github.com/tutorcruncher/django-jinja-bootstrap-form <https://github.com/tutorcruncher/django-jinja-bootstrap-form>`_

Port of `django-bootstrap-form <https://github.com/tzangms/django-bootstrap-form>`_
which is compatible with `django-jinja <https://github.com/niwibe/django-jinja>`_.

To install:

.. code-block:: shell

    pip install django-jinja-bootstrap-form
"""

template_files = [
    'templates/bootstrapform/field.jinja',
    'templates/bootstrapform/field_macros.jinja',
    'templates/bootstrapform/form.jinja',
    'templates/bootstrapform/formset.jinja',
]

setup(
    name='django-jinja-bootstrap-form',
    version=str(VERSION),
    description='django-jinja-bootstrap-form',
    long_description=description,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='bootstrap,django,jinja2',
    author='Samuel Colvin',
    author_email='s@muelcolvin.com',
    url='https://github.com/tutorcruncher/django-jinja-bootstrap-form',
    license='BSD',
    install_requires=[
        'django>=3.1',
        'django-jinja>=2.6.0',
    ],
    packages=find_packages(),
    package_data={'bootstrapform_jinja': template_files},
    python_requires='>=3.8',
    zip_safe=True,
)

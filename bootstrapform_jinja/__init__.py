from .meta import VERSION
import django

__version__ = str(VERSION)
if django.VERSION >= (3, 2):
    # The declaration is only needed for older Django versions
    pass
else:
    default_app_config = 'bootstrapform_jinja.apps.BootstrapformJinjaConfig'

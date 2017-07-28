from django.apps import AppConfig


class BootstrapformJinjaConfig(AppConfig):
    name = 'bootstrapform_jinja'
    verbose_name = 'Bootstrapform for Jinja'

    def ready(self):
        # Make sure tags are registered
        from .templatetags import bootstrap  # NOQA

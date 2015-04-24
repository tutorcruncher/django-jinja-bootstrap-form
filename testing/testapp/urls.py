from django.conf.urls import patterns, url
from .views import simple_bs_form, horizontal_bs_form

urlpatterns = patterns('',
                       url(r'^simple_bs_form/$', simple_bs_form),
                       url(r'^horizontal_bs_form/$', horizontal_bs_form)
                       )

from django.conf.urls import url
from .views import simple_bs_form, horizontal_bs_form, partial_bs_form

urlpatterns = [
    url(r'^simple_bs_form/$', simple_bs_form),
    url(r'^horizontal_bs_form/$', horizontal_bs_form),
    url(r'^partial_bs_form/$', partial_bs_form),
]

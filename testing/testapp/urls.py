from django.urls import re_path
from .views import simple_bs_form, horizontal_bs_form, partial_bs_form

urlpatterns = [
    re_path(r'^simple_bs_form/$', simple_bs_form),
    re_path(r'^horizontal_bs_form/$', horizontal_bs_form),
    re_path(r'^partial_bs_form/$', partial_bs_form),
]

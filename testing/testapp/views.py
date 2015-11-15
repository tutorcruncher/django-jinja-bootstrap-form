from django.shortcuts import render_to_response

from .forms import ExampleForm


def simple_bs_form(request):
    form = ExampleForm()
    return render_to_response('simple_bs_form.jinja', {'form': form})


def horizontal_bs_form(request):
    form = ExampleForm()
    return render_to_response('horizontal_bs_form.jinja', {'form': form})


def partial_bs_form(request):
    form = ExampleForm()
    return render_to_response('partial_bs_form.jinja', {'form': form})

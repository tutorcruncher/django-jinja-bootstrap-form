from django.shortcuts import render

from .forms import ExampleForm


def simple_bs_form(request):
    form = ExampleForm()
    return render(request, 'simple_bs_form.jinja', {'form': form})


def horizontal_bs_form(request):
    form = ExampleForm()
    return render(request, 'horizontal_bs_form.jinja', {'form': form})


def partial_bs_form(request):
    form = ExampleForm()
    return render(request, 'partial_bs_form.jinja', {'form': form})

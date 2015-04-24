from django import forms
from django.template.loader import get_template
from django_jinja import library
from django.utils.safestring import mark_safe

from bootstrapform_jinja import config


@library.filter
def bootstrap(element):
    markup_classes = {'label': '', 'value': '', 'single_value': ''}
    return render(element, markup_classes)


@library.filter
def bootstrap_inline(element):
    markup_classes = {'label': 'sr-only', 'value': '', 'single_value': ''}
    return render(element, markup_classes)


@library.filter
def bootstrap_horizontal(element, label_cols={}):
    if not label_cols:
        label_cols = 'col-sm-2 col-lg-2'

    markup_classes = {
        'label': label_cols,
        'value': '',
        'single_value': ''
    }

    for cl in label_cols.split(' '):
        split_class = cl.split('-')

        try:
            value_nb_cols = int(split_class[-1])
        except ValueError:
            value_nb_cols = config.BOOTSTRAP_COLUMN_COUNT

        if value_nb_cols >= config.BOOTSTRAP_COLUMN_COUNT:
            split_class[-1] = config.BOOTSTRAP_COLUMN_COUNT
        else:
            offset_class = cl.split('-')
            offset_class[-1] = 'offset-' + str(value_nb_cols)
            split_class[-1] = str(config.BOOTSTRAP_COLUMN_COUNT - value_nb_cols)
            markup_classes['single_value'] += ' ' + '-'.join(offset_class)
            markup_classes['single_value'] += ' ' + '-'.join(split_class)

        markup_classes['value'] += ' ' + '-'.join(split_class)

    return render(element, markup_classes)


def add_input_classes(field):
    if not is_checkbox(field) and not is_multiple_checkbox(field) and not is_radio(field) and not is_file(field):
        field_classes = field.field.widget.attrs.get('class', '')
        field_classes += ' form-control'
        field.field.widget.attrs['class'] = field_classes


def render(element, markup_classes):
    element_type = element.__class__.__name__.lower()

    if element_type == 'boundfield':
        add_input_classes(element)
        template = get_template('bootstrapform/field.jinja')
        context = {'field': element, 'form': element.form, 'classes': markup_classes}
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            for form in element.forms:
                for field in form.visible_fields():
                    add_input_classes(field)

            template = get_template('bootstrapform/formset.jinja')
            context = {'formset': element, 'classes': markup_classes}
        else:
            for field in element.visible_fields():
                add_input_classes(field)

            template = get_template('bootstrapform/form.jinja')
            context = {'form': element, 'classes': markup_classes}

    return mark_safe(template.render(context))


@library.filter
def bootstrap_classes(field):
    add_input_classes(field)
    return mark_safe(field)


@library.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@library.filter
def is_multiple_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@library.filter
def is_radio(field):
    return isinstance(field.field.widget, forms.RadioSelect)


@library.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)

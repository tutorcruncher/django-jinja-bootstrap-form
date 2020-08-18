from collections import OrderedDict
from django.forms import BoundField, CheckboxInput, CheckboxSelectMultiple, FileInput, RadioSelect
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django_jinja import library

from bootstrapform_jinja.config import BOOTSTRAP_COLUMN_COUNT


@library.test
def checkbox_field(field):
    """
    Jinja test to check if a field is a checkbox
    """
    return isinstance(field.field.widget, CheckboxInput)


@library.test
def multiple_checkbox_field(field):
    """
    Jinja test to check if a field is a multiple value checkbox
    """
    return isinstance(field.field.widget, CheckboxSelectMultiple)


@library.test
def radio_field(field):
    """
    Jinja test to check if a field is a radio select
    """
    return isinstance(field.field.widget, RadioSelect)


def add_input_classes(field):
    """
    Add form-control to class attribute of the widget of the given field.
    """
    if not isinstance(field.field.widget, (CheckboxInput, CheckboxSelectMultiple, RadioSelect, FileInput)):
        attrs = field.field.widget.attrs
        attrs['class'] = attrs.get('class', '') + ' form-control'


@library.filter
def bootstrap(element):
    """
    Render field, form or formset with bootstrap styles
    """
    return render(element)


@library.filter
def bootstrap_inline(element):
    """
    Render field, form or formset with bootstrap styles in single line
    """
    return render(element, {'label': 'sr-only'})


@library.filter
def bootstrap_horizontal(element, label_cols=None, max_columns=None):
    """
    Render field, form or formset with bootstrap styles in horizontal layout
    """
    if not label_cols:
        label_cols = ('col-sm-2', 'col-lg-2')
    if isinstance(label_cols, str):
        label_cols = label_cols.split()
    # ensure that label_cols includes only strings and doesn't have duplicates
    label_cols = tuple(OrderedDict.fromkeys(map(str, label_cols)).keys())

    if not max_columns:
        max_columns = BOOTSTRAP_COLUMN_COUNT

    cls_value = []
    cls_single_value = []

    for cl in label_cols:
        base, sep, value_nb_cols = cl.rpartition('-')
        prefix = base + sep
        try:
            value_nb_cols = int(value_nb_cols)
        except ValueError:
            value_nb_cols = max_columns

        if value_nb_cols >= max_columns:
            split_class = prefix + str(max_columns)
        else:
            offset_class = prefix + 'offset-' + str(value_nb_cols)
            split_class = prefix + str(max_columns - value_nb_cols)
            cls_single_value.extend((split_class, offset_class))

        cls_value.append(split_class)

    classes = {
        'label': ' '.join(label_cols),
        'value': ' '.join(cls_value),
        'single_value': ' '.join(cls_single_value),
    }
    return render(element, classes)


def render(element, markup_classes=None):
    """
    Internal render function used by boostrap filters
    """
    classes = {'label': '', 'value': '', 'single_value': ''}
    if markup_classes:
        classes.update(markup_classes)

    if isinstance(element, BoundField):
        # InputField
        add_input_classes(element)
        template = get_template('bootstrapform/field.jinja')
        context = {'field': element, 'form': element.form, 'classes': classes}
    elif getattr(element, 'management_form', None):
        # FormSet
        for form in element.forms:
            for field in form.visible_fields():
                add_input_classes(field)

        template = get_template('bootstrapform/formset.jinja')
        context = {'formset': element, 'classes': classes}
    else:
        # Form
        for field in element.visible_fields():
            add_input_classes(field)

        template = get_template('bootstrapform/form.jinja')
        context = {'form': element, 'classes': classes}

    return mark_safe(template.render(context))


@library.filter
def bootstrap_classes(field):
    """
    Filter that adds form-control to given input field
    """
    add_input_classes(field)
    return mark_safe(field)

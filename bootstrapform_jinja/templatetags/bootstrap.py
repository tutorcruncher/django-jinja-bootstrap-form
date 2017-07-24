from django.forms import CheckboxInput, CheckboxSelectMultiple, FileInput, RadioSelect
try:
    from django.forms.boundfield import BoundField
except ImportError:
    from django.forms.forms import BoundField
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django_jinja import library

from bootstrapform_jinja import config


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

from django import forms

__all__ = (
    'BootstrapMixin',
)

class BootstrapMixin:
    """
    Add the base Bootstrap CSS classes to form elements.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field.required and not isinstance(field.widget, forms.FileInput):
                field.widget.attrs['required'] = 'required'
            if 'placeholder' not in field.widget.attrs and field.label is not None:
                field.widget.attrs['placeholder'] = field.label

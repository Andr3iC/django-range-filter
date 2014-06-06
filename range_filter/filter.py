# -*- coding: utf-8 -*-


from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.forms import NumberInput
from django.db import models
from django.utils.translation import ugettext as _


class BaseRangeFilter(admin.filters.FieldListFilter):

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg_since = '%s__gte' % field_path
        self.lookup_kwarg_upto = '%s__lte' % field_path
        super(BaseRangeFilter, self)\
            .__init__(field, request, params, model, model_admin, field_path)
        self.form = self.get_form(request)

    def choices(self, cl):
        choices = []
        args = self.expected_parameters()
        for name, value in cl.params.items():
            if name not in args:
                choices.append({'name': name, 'value': value})
        return choices

    def expected_parameters(self):
        return [self.lookup_kwarg_since, self.lookup_kwarg_upto]

    def get_form(self, request):
        return self.form(data=self.used_parameters,
                         field_name=self.field_path)

    def queryset(self, request, queryset):
        if self.form.is_valid():
            filter_params = dict(filter(lambda x: bool(x[1]),
                                        self.form.cleaned_data.items()))
            return queryset.filter(**filter_params)
        else:
            return queryset


# DecimalRangeFilter
class DecimalRangeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        field_name = kwargs.pop('field_name')
        super(DecimalRangeForm, self).__init__(*args, **kwargs)

        self.fields['%s__gte' % field_name] = forms.DecimalField(label='',
                                                                 widget=NumberInput(
                                                                     attrs={
                                                                         'placeholder': _('>='),
                                                                         'style': 'width: 50px',
                                                                     }),
                                                                 required=False)

        self.fields['%s__lte' % field_name] = forms.DecimalField(label='',
                                                                 widget=NumberInput(
                                                                     attrs={
                                                                         'placeholder': _('<='),
                                                                         'style': 'width: 50px',
                                                                     }),
                                                                 required=False)

class DecimalRangeFilter(BaseRangeFilter):
    template = 'range_filter/decimal_range_filter.html'
    form = DecimalRangeForm


# DateRangeFilter
class DateRangeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        field_name = kwargs.pop('field_name')
        super(DateRangeForm, self).__init__(*args, **kwargs)

        self.fields['%s__gte' % field_name] = forms.DateField(
            label='', widget=AdminDateWidget(
                attrs={'placeholder': _('From date')}), localize=True,
            required=False)

        self.fields['%s__lte' % field_name] = forms.DateField(
            label='', widget=AdminDateWidget(
                attrs={'placeholder': _('To date')}), localize=True,
            required=False)


class DateRangeFilter(BaseRangeFilter):
    template = 'range_filter/date_range_filter.html'
    form = DateRangeForm


# DateTimeRangeFilter
class DateTimeRangeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        field_name = kwargs.pop('field_name')
        super(DateTimeRangeForm, self).__init__(*args, **kwargs)
        self.fields['%s__gte' % field_name] = forms.DateTimeField(
            label='',
            widget=AdminSplitDateTime(
                attrs={'placeholder': _('From Date')}
            ),
            localize=True,
            required=False)


class DateTimeRangeFilter(BaseRangeFilter):
    template = 'range_filter/date_range_filter.html'
    form = DateTimeRangeForm


# register the filters
admin.filters.FieldListFilter.register(
    lambda f: isinstance(f, models.DateField), DateRangeFilter)
admin.filters.FieldListFilter.register(
    lambda f: isinstance(f, models.DateTimeField), DateTimeRangeFilter)
admin.filters.FieldListFilter.register(
    lambda f: isinstance(f, models.DecimalField), DecimalRangeFilter)

# events/filters.py

import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    # This filter will be used to exclude sports events
    exclude_sports = django_filters.BooleanFilter(
        method='filter_exclude_sports',
        label='Exclude sports events'
    )

    class Meta:
        model = Event
        fields = ['category','status']

    def filter_exclude_sports(self, queryset, name, value):
        if value:
            return queryset.exclude(category='Sports')
        return queryset
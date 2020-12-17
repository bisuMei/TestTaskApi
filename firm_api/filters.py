import django_filters
from .models import Position


class PositionFilter(django_filters.FilterSet):
    class Meta:
        model = Position
        fields = ['position']

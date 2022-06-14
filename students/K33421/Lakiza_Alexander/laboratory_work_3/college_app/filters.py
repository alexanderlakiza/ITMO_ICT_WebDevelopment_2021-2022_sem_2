from django_filters import rest_framework as filters
from .models import *


class TeacherRoomRangeFilter(filters.FilterSet):
    room = filters.RangeFilter()
    ordering = filters.OrderingFilter(
        fields=(
            ('room', 'room'),
        )
    )

    class Meta:
        model = Teacher
        fields = ['room']

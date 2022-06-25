from django_filters import rest_framework as filters
from .models import *


class TeacherRoomRangeFilter(filters.FilterSet):
    room_min = filters.NumberFilter(field_name="room", lookup_expr='gte')
    room_max = filters.NumberFilter(field_name="room", lookup_expr='lte')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'room', 'subjects__name']


class MarksFilters(filters.FilterSet):
    mark_min = filters.NumberFilter(field_name="mark", lookup_expr='gte')
    mark_max = filters.NumberFilter(field_name="mark", lookup_expr='lte')

    class Meta:
        model = Mark
        fields = ['student__last_name', 'student__first_name', 'mark', 'subject__name', 'student__group__name']


class PairsFilters(filters.FilterSet):
    room_min = filters.NumberFilter(field_name="room", lookup_expr='gte')
    room_max = filters.NumberFilter(field_name="room", lookup_expr='lte')

    n_lesson_min = filters.NumberFilter(field_name="pair_number", lookup_expr='gte')
    n_lesson_max = filters.NumberFilter(field_name="pair_number", lookup_expr='lte')

    class Meta:
        model = Pair
        fields = ['subject__name', 'group__name', 'pair_number', 'room', 'name_day', 'teacher__last_name']

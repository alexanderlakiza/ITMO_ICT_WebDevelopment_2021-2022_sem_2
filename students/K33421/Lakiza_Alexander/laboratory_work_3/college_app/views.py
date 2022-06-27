from rest_framework.authentication import TokenAuthentication
from rest_framework import filters, status
from rest_framework.generics import *
from rest_framework.views import APIView, Response
from rest_framework.permissions import *
from .serializers import *
from .filters import TeacherRoomRangeFilter, MarksFilters, PairsFilters
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend


# class IsManager(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.type == 'manager'
#
#
# class IsDeputy(BasePermission):
#     def has_permission(self, request, view):
#         # print(request.user.type)
#         return request.user.type == 'deputy'


# STUDENTS
class AllStudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListView(AllStudentListView):
    # permission_classes = [AllowAny]
    pagination_class = CustomPagination

    # filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    # search_fields = ('first_name', 'last_name', 'group__name',)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['first_name', 'last_name', 'group__name']
    filterset_fields = ['first_name', 'last_name', 'group__name']


class StudentAllView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsDeputy]


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsDeputy]


# TEACHERS
class AllTeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherListView(AllTeacherListView):
    # permission_classes = [AllowAny]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['first_name', 'last_name', 'room', 'subjects__name']
    filterset_fields = ['first_name', 'last_name', 'room', 'subjects__name']
    filterset_class = TeacherRoomRangeFilter


class TeacherAllView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsDeputy]


class TeacherCreateView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsDeputy]


# SUBJECTS
class AllSubjectListView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectListView(AllSubjectListView):
    # permission_classes = [AllowAny]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name',)

    pagination_class = CustomPagination


class SubjectAllView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = [IsDeputy]


class SubjectCreateView(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = [IsDeputy]


# MARKS
class MarkListView(ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkFullViewSerializer
    # permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['student__last_name', 'student__first_name', 'mark', 'subject__name', 'student__group__name']
    ordering_fields = ['student__last_name', 'student__first_name', 'mark', 'subject__name', 'student__group__name']
    filterset_class = MarksFilters

    pagination_class = CustomPagination


class MarkAllView(RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    # permission_classes = [IsDeputy]


class MarkCreateView(CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    # permission_classes = [IsDeputy]


# PAIRS
class AllPairListView(ListAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer


class PairListView(ListAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairFullViewSerializer
    # permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    filterset_fields = ['subject__name', 'group__name', 'pair_number', 'room', 'name_day', 'teacher__last_name']
    ordering_fields = ['subject__name', 'group__name', 'pair_number', 'room', 'teacher__last_name']
    filterset_class = PairsFilters

    pagination_class = CustomPagination


class PairAllView(RetrieveUpdateDestroyAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer
    # permission_classes = [IsManager]


class PairCreateView(CreateAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer
    # permission_classes = [IsManager]


# SubjectToTeacher
class SubjectToTeacherListView(ListAPIView):
    queryset = SubjectToTeacher.objects.all()
    serializer_class = SubjectToTeacherSerializer
    # permission_classes = [AllowAny]


class SubjectToTeacherAllView(RetrieveUpdateDestroyAPIView):
    queryset = SubjectToTeacher.objects.all()
    serializer_class = SubjectToTeacherSerializer
    # permission_classes = [IsDeputy]


class SubjectToTeacherCreateView(CreateAPIView):
    queryset = SubjectToTeacher.objects.all()
    serializer_class = SubjectToTeacherSerializer
    # permission_classes = [IsDeputy]


# GROUPS
class AllGroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupListView(AllGroupListView):
    # permission_classes = [AllowAny]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name',)

    pagination_class = CustomPagination


class GroupCreateView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [IsDeputy]


class GroupAllView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [IsDeputy]


# StudentToGroup
class StudentToGroupListView(ListAPIView):
    queryset = StudentToGroup.objects.all()
    serializer_class = StudentToGroupSerializer
    # permission_classes = [AllowAny]


class StudentToGroupAllView(RetrieveUpdateDestroyAPIView):
    queryset = StudentToGroup.objects.all()
    serializer_class = StudentToGroupSerializer
    # permission_classes = [IsDeputy]


class StudentToGroupCreateView(CreateAPIView):
    queryset = StudentToGroup.objects.all()
    serializer_class = StudentToGroupSerializer
    # permission_classes = [IsDeputy]


# GroupToSpecialty
class GrToSpecListView(ListAPIView):
    queryset = GroupToSpecialty.objects.all()
    serializer_class = GroupToSpecialtySerializer


class GrToSpecAllView(RetrieveUpdateDestroyAPIView):
    queryset = GroupToSpecialty.objects.all()
    serializer_class = GroupToSpecialtySerializer
    # permission_classes = [IsDeputy]


class GrToSpecCreateView(CreateAPIView):
    queryset = GroupToSpecialty.objects.all()
    serializer_class = GroupToSpecialtySerializer
    # permission_classes = [IsDeputy]


# SPECIALTY
class SpecialtyFullView(ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class SpecialtyListView(ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'groups__name']
    filterset_fields = ['name', 'groups__name', 'it_specialty']
    pagination_class = CustomPagination


class SpecialtyALlView(RetrieveUpdateDestroyAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class SpecialtyCreateView(CreateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    # permission_classes = [IsDeputy]


# HAND-MADE FILTERS
class StudentsByGroupListView(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        students_queryset = Student.objects.all()
        group_name = self.request.query_params.get('group')
        group_id = Group.objects.all().get(name=group_name).id

        if group_id:
            students_queryset = students_queryset.filter(group=group_id)

        return students_queryset


class PairByDayGroupListView(ListAPIView):
    serializer_class = PairSerializer

    def get_queryset(self):
        day_name = self.request.query_params.get('day')
        group_name = self.request.query_params.get('group')
        group_id = Group.objects.all().get(name=group_name).id

        pair_queryset = Pair.objects.all()
        if group_id and day_name:
            pair_queryset = pair_queryset.filter(name_day=day_name, group=group_id)

        return pair_queryset


class PairByRoomDayListView(ListAPIView):
    serializer_class = PairSerializer

    def get_queryset(self):
        pair_queryset = Pair.objects.all()
        user = self.request.user

        if user.is_authenticated:
            room_num = self.request.query_params.get('room')
            day_name = self.request.query_params.get('day')

            if room_num and day_name:
                pair_queryset = pair_queryset.filter(room=room_num, name_day=day_name)

        return pair_queryset


# AUTO FILTERS
class MarkOrderedFilterView(ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    filter_backends = (filters.OrderingFilter,)
    filterset_fields = ('mark',)


class StudentSearchFilterView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('last_name',)


class TeacherRoomRangeFilterView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherRoomRangeFilter

    # CUSTOM PAGINATION
    pagination_class = CustomPagination


# FILE UPLOAD
class StudentPhotoCreateView(CreateAPIView):
    queryset = StudentPhoto.objects.all()
    serializer_class = StudentPhotoSerializer


class MultipleStudentPhotoCreateView(CreateAPIView):
    queryset = StudentPhoto.objects.all()
    serializer_class = StudentPhotoSerializer

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')

        for file in files:
            student_id = request.POST.get('student')
            file = StudentPhoto(
                student=Student.objects.get(id=student_id),
                file=file)
            file.save()

        return Response(str(request.data), status=status.HTTP_201_CREATED)

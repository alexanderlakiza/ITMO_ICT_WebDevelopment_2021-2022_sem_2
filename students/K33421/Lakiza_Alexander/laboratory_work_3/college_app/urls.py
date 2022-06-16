from django.urls import path
from .views import *

app_name = "college_app"

urlpatterns = [
    path('pair/list/', PairListView.as_view()),
    path('pair/<int:pk>/', PairAllView.as_view(), name='pair'),
    path('pair/create/', PairCreateView.as_view(), name='pair_create'),

    path('student/list/', StudentListView.as_view()),
    path('student/<int:pk>/', StudentAllView.as_view(), name='student'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),

    path('teacher/list/', TeacherListView.as_view()),
    path('teacher/<int:pk>/', TeacherAllView.as_view(), name='teacher'),
    path('teacher/create/', TeacherCreateView.as_view()),

    path('subject/list/', SubjectListView.as_view()),
    path('subject/<int:pk>/', SubjectAllView.as_view(), name='subject'),
    path('subject/create/', SubjectCreateView.as_view()),

    path('subteach/list/', SubjectToTeacherListView.as_view()),
    path('subteach/<int:pk>/', SubjectToTeacherAllView.as_view()),
    path('subteach/create/', SubjectToTeacherCreateView.as_view()),

    path('mark/list/', MarkListView.as_view()),
    path('mark/<int:pk>/', MarkAllView.as_view()),
    path('mark/create/', MarkCreateView.as_view(), name='mark_create'),

    path('group/list/', GroupListView.as_view()),
    path('group/<int:pk>/', GroupAllView.as_view(), name='group'),
    path('group/create/', GroupCreateView.as_view()),

    path('stugroup/list/', StudentToGroupListView.as_view()),
    path('stugroup/<int:pk>/', StudentToGroupAllView.as_view(), name='student_group'),
    path('stugroup/create/', StudentToGroupCreateView.as_view()),

    # hand filters
    path('student_by_group/', StudentsByGroupListView.as_view()),
    path('pair_by_day_group/', PairByDayGroupListView.as_view()),
    path('pair_by_day_room/', PairByRoomDayListView.as_view()),

    # auto filters
    path('mark_ordered/', MarkOrderedFilterView.as_view()),
    path('student_search/', StudentSearchFilterView.as_view()),
    path('teacher_room_range/',
         TeacherRoomRangeFilterView.as_view()),

    # file uploads
    path('student_photo_upload/', StudentPhotoCreateView.as_view()),
    path('multiple_student_photo_upload/', MultipleStudentPhotoCreateView.as_view())
]

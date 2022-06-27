from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SubjectPartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name"]


class GroupPartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class TeacherSerializer(serializers.ModelSerializer):
    subjects = SubjectPartedSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    group = GroupPartedSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = "__all__"


class StudentPartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class MarkFullViewSerializer(serializers.ModelSerializer):
    subject = SubjectPartedSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Mark
        fields = "__all__"


class PairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = "__all__"


class TeacherPartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "first_name", 'last_name']


class PairFullViewSerializer(serializers.ModelSerializer):
    subject = SubjectPartedSerializer(read_only=True)
    teacher = TeacherPartedSerializer(read_only=True)
    group = GroupPartedSerializer(read_only=True)

    class Meta:
        model = Pair
        fields = "__all__"


class PairPartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = ["id", "pair_number", "subject", "teacher", "room"]


class SubjectToTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectToTeacher
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class StudentToGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentToGroup
        fields = "__all__"


class StudentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPhoto
        fields = ['student', 'file']


class GroupToSpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupToSpecialty
        fields = "__all__"


class SpecialtySerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = Specialty
        fields = "__all__"

from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_file_type, validate_file_size


class User(AbstractUser):
    type_choices = [
        ('admin', 'администратор'),
        ('deputy', 'замдекана'),
        ('manager', 'диспетчер'),
    ]
    type = models.CharField(max_length=50, choices=type_choices, verbose_name='Тип')

    REQUIRED_FIELDS = ('type', 'first_name', 'last_name')

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subjects = models.ManyToManyField('Subject', through='SubjectToTeacher')
    room = models.CharField(max_length=10)
    old_room = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class SubjectToTeacher(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.teacher, self.subject)


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class StudentToGroup(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.student, self.group)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group = models.ManyToManyField('Group', through='StudentToGroup')

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Mark(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.student.last_name, self.subject)


class Pair(models.Model):
    day_choices = [
        ('Mon', 'Понедельник'),
        ('Tue', 'Вторник'),
        ('Wed', 'Среда'),
        ('Thu', 'Четверг'),
        ('Fri', 'Пятница'),
        ('Sat', 'Суббота'),
        ('Sun', 'Воскресенье'),
    ]
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    pair_number = models.IntegerField()
    name_day = models.CharField(max_length=30, choices=day_choices)
    room = models.IntegerField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} пара №'.format(self.name_day, self.group, self.pair_number)


def get_upload_path(instance, filename):
    return f'students_photos/photos_of_student_{instance.student.id}/{filename}'


class StudentPhoto(models.Model):
    student = models.ForeignKey('Student',
                                    on_delete=models.CASCADE,
                                    related_name='student_photos')
    file = models.FileField(
        validators=[validate_file_size, validate_file_type],
        upload_to=get_upload_path
    )
    file_name = models.CharField(max_length=100, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Photo of {str(self.student)}'

    def save(self, *args, **kwargs):
        self.file_name = self.file.name
        self.file_size = self.file.size
        super(StudentPhoto, self).save(*args, **kwargs)

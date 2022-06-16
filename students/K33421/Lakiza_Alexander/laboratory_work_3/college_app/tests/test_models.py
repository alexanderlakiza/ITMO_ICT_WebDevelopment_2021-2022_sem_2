from django.test import TestCase
from django.db.models import IntegerField
from ..models import *


class SubjectNameModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Subject.objects.create(
            name='Математика',
        )

    def test_medal_field_value(self):
        subject_instance = Subject.objects.get(id=1)
        self.assertEquals(subject_instance.name, 'Математика')


class GroupNameLengthModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(
            name='K33421'
        )

    def test_passport_max_length(self):
        group_instance = Group.objects.get(id=1)
        max_length = group_instance._meta.get_field('name').max_length
        self.assertEquals(max_length, 40)


class PairFieldTypeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Teacher.objects.create(
            first_name='Светлана',
            last_name='Козлова'
        )

        Group.objects.create(
            name='K33421'
        )

        Subject.objects.create(
            name='Математика',
        )

        Pair.objects.create(
            name_day='Fri',
            room=31,
            group=Group.objects.get(id=1),
            pair_number=4,
            teacher=Teacher.objects.get(id=1),
            subject=Subject.objects.get(id=1)
        )

    def test_vaccinated_field_type(self):
        pair_instance = Pair.objects.get(id=1)
        room_filed = pair_instance._meta.get_field('room')
        self.assertTrue(isinstance(room_filed, IntegerField))

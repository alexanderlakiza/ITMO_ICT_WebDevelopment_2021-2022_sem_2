from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Student)
def create_participant(sender, instance, created, **kwargs):
    if created:
        print(f'Student {instance.first_name} {instance.last_name} created\n')


@receiver(pre_save, sender=Teacher)
def update_teacher_room(sender, instance, **kwargs):
    prev_instance = Teacher.objects.get(id=instance.id)
    instance.old_room = prev_instance.room
    print(f'Room number for  Teacher - {instance.first_name} {instance.last_name} updated: \n'
          f'Room number was: {instance.old_room}\n'
          f'Room number now: {instance.room}\n')


@receiver(pre_delete, sender=Student)
def delete_participant(sender, instance, **kwargs):
    with open('deleted_participants_log.txt', 'a') as f:
        f.write(f'Student {instance.first_name} {instance.last_name} deleted\n')

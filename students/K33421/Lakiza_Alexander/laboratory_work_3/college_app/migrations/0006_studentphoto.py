# Generated by Django 4.0.4 on 2022-06-15 15:49

import college_app.models
import college_app.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0005_teacher_old_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=college_app.models.get_upload_path, validators=[college_app.validators.validate_file_size, college_app.validators.validate_file_type])),
                ('file_name', models.CharField(blank=True, max_length=100, null=True)),
                ('file_size', models.IntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_photos', to='college_app.student')),
            ],
        ),
    ]

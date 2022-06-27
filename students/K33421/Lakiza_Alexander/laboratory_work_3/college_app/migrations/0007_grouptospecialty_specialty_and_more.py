# Generated by Django 4.0.4 on 2022-06-26 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0006_studentphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupToSpecialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_app.group')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('it_specialty', models.BooleanField()),
                ('groups', models.ManyToManyField(through='college_app.GroupToSpecialty', to='college_app.group')),
            ],
        ),
        migrations.AddField(
            model_name='grouptospecialty',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_app.specialty'),
        ),
    ]

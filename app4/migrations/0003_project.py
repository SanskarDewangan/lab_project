# Generated by Django 5.0.2 on 2024-07-16 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0002_alter_course_course_credits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptopic', models.CharField(max_length=200)),
                ('plangauges', models.CharField(max_length=200)),
                ('pduration', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.student')),
            ],
        ),
    ]

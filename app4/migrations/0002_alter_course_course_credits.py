# Generated by Django 5.0.2 on 2024-07-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_credits',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

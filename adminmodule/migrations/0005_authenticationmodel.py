# Generated by Django 5.1 on 2024-09-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0004_remove_designationmodel_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]

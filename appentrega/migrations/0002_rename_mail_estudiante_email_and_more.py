# Generated by Django 5.0.7 on 2024-08-02 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appentrega', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='mail',
            new_name='email',
        ),
    ]
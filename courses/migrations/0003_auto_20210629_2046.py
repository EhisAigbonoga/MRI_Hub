# Generated by Django 3.0 on 2021-06-29 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorization',
        ),
        migrations.AlterModelOptions(
            name='categorization',
            options={'ordering': ['-updated'], 'verbose_name': 'Categorization', 'verbose_name_plural': 'Categorizations'},
        ),
    ]

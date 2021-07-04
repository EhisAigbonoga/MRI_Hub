# Generated by Django 3.0 on 2021-06-28 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crihhome', '0012_remove_medicalinnovationcourses_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank='', editable=False, max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(default='', upload_to='post_image')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateField()),
                ('slug', models.SlugField(blank='', editable=False, max_length=100)),
                ('status', models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft')], default='Draft', max_length=10)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crihhome.Category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-updated'],
            },
        ),
        migrations.DeleteModel(
            name='ConferencenFellowships',
        ),
        migrations.DeleteModel(
            name='GrantsnContest',
        ),
        migrations.DeleteModel(
            name='InternshipsnScholarships',
        ),
        migrations.DeleteModel(
            name='Latest',
        ),
        migrations.DeleteModel(
            name='MedicalInnovationCourses',
        ),
        migrations.DeleteModel(
            name='ResearchCourses',
        ),
    ]
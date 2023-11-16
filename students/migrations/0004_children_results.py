# Generated by Django 4.2.7 on 2023-11-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_userreg_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Children_Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=255)),
                ('child_surname', models.CharField(max_length=255)),
                ('child_parentname', models.CharField(max_length=255)),
                ('child_grade', models.CharField(max_length=255)),
                ('child_email', models.CharField(max_length=255)),
                ('child_corrects', models.CharField(max_length=255)),
                ('child_wrongs', models.CharField(max_length=255)),
                ('child_answers', models.CharField(max_length=1000)),
                ('child_correctornot', models.CharField(max_length=1000)),
                ('correct_answersoftest', models.CharField(max_length=1000)),
            ],
        ),
    ]

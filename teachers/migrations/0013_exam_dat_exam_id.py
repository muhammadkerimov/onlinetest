# Generated by Django 4.2.7 on 2023-11-16 22:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0012_alter_exam_dat_exam_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_dat',
            name='exam_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]

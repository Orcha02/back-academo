# Generated by Django 3.2.13 on 2022-10-08 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20221008_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='max_score',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=6, verbose_name='Max Score'),
        ),
    ]

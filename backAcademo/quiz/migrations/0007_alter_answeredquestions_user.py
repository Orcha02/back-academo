# Generated by Django 3.2.13 on 2022-10-08 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0006_question_max_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeredquestions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attempts', to=settings.AUTH_USER_MODEL),
        ),
    ]

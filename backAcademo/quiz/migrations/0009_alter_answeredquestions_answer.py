# Generated by Django 3.2.13 on 2022-10-08 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_alter_answeredquestions_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeredquestions',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.chooseanswer'),
        ),
    ]

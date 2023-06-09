# Generated by Django 4.1.5 on 2023-01-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "instructor",
            "0002_livetime_quizpost_attempt_count_quizpost_difficulty_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="livetime",
            name="close_time",
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name="livetime",
            name="start_time",
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name="quizpost",
            name="total_marks",
            field=models.IntegerField(default=100),
        ),
    ]

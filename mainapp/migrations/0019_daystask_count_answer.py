# Generated by Django 3.0.1 on 2020-03-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20200324_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='daystask',
            name='count_answer',
            field=models.IntegerField(default=0),
        ),
    ]

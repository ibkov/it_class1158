# Generated by Django 3.0.1 on 2020-03-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_auto_20200325_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daystask',
            name='id_answers',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='ID учеников, кто дал правильный ответ'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191118_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_classes',
            field=models.ManyToManyField(to='core.StudentClass'),
        ),
        migrations.AddField(
            model_name='user',
            name='subjects',
            field=models.ManyToManyField(to='core.Subject'),
        ),
    ]

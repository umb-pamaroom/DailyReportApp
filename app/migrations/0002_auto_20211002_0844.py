# Generated by Django 3.2.7 on 2021-10-01 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='best',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='memo',
            name='discovery',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='memo',
            name='dislike',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='memo',
            name='happy',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='memo',
            name='other',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='memo',
            name='summarize',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='memo',
            name='tired',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='memo',
            name='tomorrow',
            field=models.TextField(blank=True),
        ),
    ]

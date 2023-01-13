# Generated by Django 3.2.12 on 2023-01-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0002_language'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistrequest',
            name='language',
        ),
        migrations.AddField(
            model_name='artistrequest',
            name='languages',
            field=models.ManyToManyField(blank=True, default='', to='misc.Language'),
        ),
        migrations.RemoveField(
            model_name='artist',
            name='languages',
        ),
        migrations.AddField(
            model_name='artist',
            name='languages',
            field=models.ManyToManyField(blank=True, default='', to='misc.Language'),
        ),
    ]
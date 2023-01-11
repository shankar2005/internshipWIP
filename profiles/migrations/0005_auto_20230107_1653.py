# Generated by Django 3.2.12 on 2023-01-07 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20230107_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='agreement',
            field=models.URLField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='amNotes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='attitudeRating',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='budgetIdea',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='budgetRange',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='hasManager',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='manager',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='profiles.manager'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='phone',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='pmNotes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='profesionalRating',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='socialLinks',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='worksLink',
            field=models.ManyToManyField(blank=True, default='', to='profiles.Work'),
        ),
    ]
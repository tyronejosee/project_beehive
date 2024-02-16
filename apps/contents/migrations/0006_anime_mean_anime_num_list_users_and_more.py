# Generated by Django 5.0.1 on 2024-02-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_alter_manga_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='mean',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean'),
        ),
        migrations.AddField(
            model_name='anime',
            name='num_list_users',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of List Users'),
        ),
        migrations.AddField(
            model_name='anime',
            name='num_scoring_users',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Scoring Users'),
        ),
        migrations.AddField(
            model_name='anime',
            name='popularity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Popularity'),
        ),
        migrations.AddField(
            model_name='anime',
            name='rank',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rank'),
        ),
        migrations.AddField(
            model_name='manga',
            name='mean',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean'),
        ),
        migrations.AddField(
            model_name='manga',
            name='num_list_users',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of List Users'),
        ),
        migrations.AddField(
            model_name='manga',
            name='num_scoring_users',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Scoring Users'),
        ),
        migrations.AddField(
            model_name='manga',
            name='popularity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Popularity'),
        ),
        migrations.AddField(
            model_name='manga',
            name='rank',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rank'),
        ),
    ]
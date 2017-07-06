# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-04 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_km', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('latitude_with_road', models.FloatField()),
                ('longitude_with_road', models.FloatField()),
            ],
        ),
        migrations.AlterIndexTogether(
            name='sector',
            index_together=set([('x', 'y')]),
        ),
        migrations.AddField(
            model_name='distance',
            name='sector1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distance1', to='distances.Sector'),
        ),
        migrations.AddField(
            model_name='distance',
            name='sector2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distance2', to='distances.Sector'),
        ),
        migrations.AlterIndexTogether(
            name='distance',
            index_together=set([('sector1', 'sector2')]),
        ),
    ]
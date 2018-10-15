# Generated by Django 2.1.1 on 2018-10-15 14:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0008_auto_20181015_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_folder',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='equipment',
            name='shot',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='plots.Shot_information'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='shot_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='n_axis',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='shot_information',
            name='aquisition_date',
            field=models.DateField(verbose_name=datetime.datetime(2018, 10, 15, 14, 44, 11, 905851, tzinfo=utc)),
        ),
    ]
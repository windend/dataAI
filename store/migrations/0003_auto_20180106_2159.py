# Generated by Django 2.0 on 2018-01-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180106_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='invertory',
            name='currentStore',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invertory',
            name='soldNum',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[(None, ' '), ('0', 'male'), ('1', 'female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='paymethod',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='referer',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='invertory',
            name='storeNum',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='soldtime',
            field=models.DateField(auto_now=True, verbose_name='sold time'),
        ),
    ]

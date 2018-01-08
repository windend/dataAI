# Generated by Django 2.0 on 2018-01-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20180106_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pbrand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pcolor',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pmodel',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='psprice',
            new_name='sprice',
        ),
        migrations.AlterField(
            model_name='invertory',
            name='currentStore',
            field=models.PositiveIntegerField(default=5, editable=False),
        ),
        migrations.AlterField(
            model_name='invertory',
            name='soldNum',
            field=models.PositiveIntegerField(default=5, editable=False),
        ),
    ]
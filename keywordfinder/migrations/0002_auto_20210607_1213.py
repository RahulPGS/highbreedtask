# Generated by Django 3.2.4 on 2021-06-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywordfinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlkeywords',
            name='description',
            field=models.TextField(default='No description found'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='urlkeywords',
            name='keywords',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='urlkeywords',
            name='og_description',
            field=models.TextField(default='No og:description found'),
            preserve_default=False,
        ),
    ]

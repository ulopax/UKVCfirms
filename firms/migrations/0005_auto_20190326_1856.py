# Generated by Django 2.1.7 on 2019-03-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0004_auto_20190326_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_current',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

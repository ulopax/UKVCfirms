# Generated by Django 2.1.7 on 2019-03-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0002_auto_20190326_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_investment',
        ),
        migrations.AddField(
            model_name='job',
            name='investment_lookup',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firm',
            old_name='alum',
            new_name='aum',
        ),
        migrations.RenameField(
            model_name='firm',
            old_name='first_name',
            new_name='firm_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]

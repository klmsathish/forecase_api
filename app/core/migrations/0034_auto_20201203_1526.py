# Generated by Django 3.1.4 on 2020-12-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20201203_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.TextField(null=True),
        ),
    ]

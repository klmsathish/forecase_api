# Generated by Django 3.1.4 on 2020-12-02 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20201202_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='storyImage',
            field=models.OneToOneField(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='core.photo'),
            preserve_default=False,
        ),
    ]

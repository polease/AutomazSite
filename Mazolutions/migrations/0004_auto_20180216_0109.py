# Generated by Django 2.0.2 on 2018-02-16 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mazolutions', '0003_auto_20180216_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mazolutionstep',
            name='reference_mazolution',
        ),
        migrations.AlterField(
            model_name='mazolutionstep',
            name='mazolution',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='Mazolutions.Mazolution'),
        ),
    ]

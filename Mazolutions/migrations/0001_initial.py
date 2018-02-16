# Generated by Django 2.0.2 on 2018-02-15 22:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mazolution',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ProblemTitle', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=50)),
                ('Block', models.CharField(max_length=255)),
                ('Context', models.CharField(max_length=2000)),
                ('SolutionOverview', models.CharField(max_length=200)),
                ('ShortcutKeyBinding', models.CharField(max_length=50)),
                ('Environment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MazolutionStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.CharField(max_length=2000)),
                ('Automation', models.CharField(max_length=2000)),
                ('ReferenceMazolution', models.ForeignKey(on_delete=None, to='Mazolutions.Mazolution')),
            ],
        ),
    ]

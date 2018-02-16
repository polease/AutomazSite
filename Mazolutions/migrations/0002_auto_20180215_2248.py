# Generated by Django 2.0.2 on 2018-02-15 22:48

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('Mazolutions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mazolution',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='mazolution',
            old_name='Block',
            new_name='block',
        ),
        migrations.RenameField(
            model_name='mazolution',
            old_name='Context',
            new_name='context',
        ),
        migrations.RenameField(
            model_name='mazolution',
            old_name='Environment',
            new_name='environment',
        ),
        migrations.RenameField(
            model_name='mazolution',
            old_name='ID',
            new_name='id', 
        ),
        migrations.RenameField(
            model_name='mazolution',
            old_name='ProblemTitle',
            new_name='problem_title',
        ),
        migrations.RenameField(
            model_name='mazolution',
            old_name='ShortcutKeyBinding',
            new_name='shortcut_key_binding',
        ),
        migrations.RenameField(
            model_name='mazolution',
            old_name='SolutionOverview',
            new_name='solution_overview',
        ),
        migrations.RenameField(
            model_name='mazolutionstep',
            old_name='Automation',
            new_name='automation',
        ),
        migrations.RenameField(
            model_name='mazolutionstep',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='mazolutionstep',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='mazolutionstep',
            old_name='Number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='mazolutionstep',
            old_name='ReferenceMazolution',
            new_name='reference_mazolution',
        ),
    ]
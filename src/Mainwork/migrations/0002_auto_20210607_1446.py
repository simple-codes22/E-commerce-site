# Generated by Django 2.1.5 on 2021-06-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainwork', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='EMail',
            new_name='e_Mail',
        ),
        migrations.AlterField(
            model_name='store',
            name='date_registered',
            field=models.DateField(),
        ),
    ]

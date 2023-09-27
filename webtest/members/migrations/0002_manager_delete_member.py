# Generated by Django 4.2.5 on 2023-09-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='NAME')),
                ('date', models.DateField(verbose_name='DATE')),
                ('time', models.TimeField(verbose_name='TIME')),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]

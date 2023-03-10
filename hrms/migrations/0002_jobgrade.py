# Generated by Django 4.1.1 on 2022-12-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobGrade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.CharField(max_length=2, unique=True)),
                ('lowest_sal', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('highest_sal', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
            ],
        ),
    ]

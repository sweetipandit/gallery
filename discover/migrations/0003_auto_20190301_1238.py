# Generated by Django 2.1.7 on 2019-03-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0002_profilemodel_profilearea'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgName', models.CharField(max_length=50)),
                ('eventTitle', models.CharField(max_length=200)),
                ('minCost', models.IntegerField()),
                ('maxCost', models.IntegerField()),
                ('contact', models.CharField(max_length=15)),
                ('eventImage', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=51)),
                ('userPhone', models.CharField(max_length=15)),
                ('userEmail', models.CharField(max_length=50)),
                ('userPassword', models.CharField(max_length=20)),
                ('userConformPassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileModel',
        ),
    ]

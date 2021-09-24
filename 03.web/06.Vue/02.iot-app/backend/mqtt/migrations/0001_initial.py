# Generated by Django 3.2.7 on 2021-09-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True, verbose_name='사용자명')),
                ('place', models.CharField(max_length=30, null=True, verbose_name='설치장소')),
                ('sensor', models.CharField(max_length=30, null=True, verbose_name='센서')),
                ('value', models.FloatField(verbose_name='센서값')),
                ('regdate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='등록일')),
            ],
        ),
    ]
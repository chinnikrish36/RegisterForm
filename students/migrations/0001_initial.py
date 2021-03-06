# Generated by Django 2.2 on 2020-02-20 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegister',
            fields=[
                ('Stu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=20)),
                ('Middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=6)),
                ('Father_name', models.CharField(max_length=20)),
                ('Standard', models.CharField(choices=[('V', 'sixth'), ('VII', 'seventh'), ('VIII', 'eight'), ('XI', 'ninth'), ('X', 'tenth')], max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

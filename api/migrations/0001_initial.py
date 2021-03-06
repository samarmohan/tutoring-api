# Generated by Django 3.1.2 on 2021-01-22 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('subjects', models.CharField(max_length=20)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutees', to='api.tutor')),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2021-01-22 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_tutee_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutee',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutees', to='api.tutor'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-15 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.College'),
        ),
    ]

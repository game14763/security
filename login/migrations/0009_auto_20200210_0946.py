# Generated by Django 2.0.1 on 2020-02-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20200210_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.IntegerField(blank=True, db_column='Id', primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.0.2 on 2022-05-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
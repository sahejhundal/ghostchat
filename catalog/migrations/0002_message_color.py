# Generated by Django 4.0.4 on 2022-05-20 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('userip', models.CharField(max_length=100)),
                ('senttime', models.DateTimeField()),
                ('content', models.TextField(help_text='Type something', max_length=1000)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-26 14:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator('[1-9a-zA-Z]\\w*[.]?\\w+@gmail[.]com')])),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
            ],
        ),
    ]

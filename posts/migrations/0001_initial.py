# Generated by Django 4.1 on 2022-08-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('body', models.TextField(blank=True, max_length=600, null=True)),
            ],
        ),
    ]

# Generated by Django 3.2.18 on 2023-03-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('disc', models.TextField()),
                ('year', models.IntegerField()),
                ('poster', models.ImageField(upload_to='pics')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
                ('Msg', models.CharField(max_length=250)),
            ],
        ),
    ]

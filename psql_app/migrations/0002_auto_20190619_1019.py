# Generated by Django 2.2.2 on 2019-06-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psql_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default='content cannot be shown'),
        ),
        migrations.AlterField(
            model_name='article',
            name='times_read',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]

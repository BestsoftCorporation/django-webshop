# Generated by Django 3.1.4 on 2021-01-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='content',
        ),
        migrations.RemoveField(
            model_name='products',
            name='num_views',
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
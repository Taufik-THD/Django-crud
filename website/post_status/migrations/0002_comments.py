# Generated by Django 2.1.3 on 2018-11-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('user_id', models.IntegerField()),
                ('status_id', models.IntegerField()),
            ],
        ),
    ]

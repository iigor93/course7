# Generated by Django 4.0.4 on 2022-06-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='chat_tgid',
            field=models.CharField(max_length=20, verbose_name='Чат id'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user_tgid',
            field=models.CharField(max_length=20, verbose_name='Пользователь id'),
        ),
    ]
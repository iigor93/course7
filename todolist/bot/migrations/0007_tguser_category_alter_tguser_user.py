# Generated by Django 4.0.4 on 2022-06-23 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0008_alter_goalcategory_board'),
        ('bot', '0006_tguser_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tg_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tg_category', to='goals.goalcategory'),
        ),
    ]

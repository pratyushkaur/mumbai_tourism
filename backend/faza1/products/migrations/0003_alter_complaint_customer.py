# Generated by Django 4.2.5 on 2023-10-04 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_cart_checked_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
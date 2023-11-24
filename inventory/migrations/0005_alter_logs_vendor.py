# Generated by Django 4.2.6 on 2023-11-01 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_item_qty_logs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.vendor'),
        ),
    ]
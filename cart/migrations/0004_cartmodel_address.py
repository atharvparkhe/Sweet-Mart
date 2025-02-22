# Generated by Django 4.1.2 on 2023-06-08 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_initial'),
        ('cart', '0003_remove_cartmodel_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selected_address', to='authentication.customeraddress'),
        ),
    ]

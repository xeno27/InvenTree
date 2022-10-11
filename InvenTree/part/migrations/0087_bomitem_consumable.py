# Generated by Django 3.2.13 on 2022-04-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0086_auto_20220912_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='bomitem',
            name='consumable',
            field=models.BooleanField(default=False, help_text='This BOM item is consumable (it is not tracked in build orders)', verbose_name='Consumable'),
        ),
    ]
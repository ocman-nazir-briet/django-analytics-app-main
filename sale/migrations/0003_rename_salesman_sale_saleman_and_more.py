# Generated by Django 4.0.1 on 2022-10-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_rename_saleman_sale_salesman_alter_sale_total_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='salesman',
            new_name='saleman',
        ),
        migrations.AlterField(
            model_name='sale',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]

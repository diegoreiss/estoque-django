# Generated by Django 4.2.6 on 2023-10-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_alter_categories_options_alter_products_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='picture',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

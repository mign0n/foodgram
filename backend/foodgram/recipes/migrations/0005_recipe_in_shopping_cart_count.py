# Generated by Django 4.2.2 on 2023-07-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0004_alter_tag_color_alter_tag_name_alter_tag_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='in_shopping_cart_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-05 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0005_recipe_in_shopping_cart_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'default_related_name': '%(class)s'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement_unit',
            field=models.CharField(
                max_length=200, verbose_name='единица измерения'
            ),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ингредиент'),
        ),
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='amount',
            field=models.IntegerField(
                verbose_name='количество ингредиента в рецепте'
            ),
        ),
        migrations.AlterField(
            model_name='ingredientinrecipe',
            name='ingredient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='recipes.ingredient',
                verbose_name='ингредиент',
            ),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(
                related_name='recipe_ingredients',
                through='recipes.IngredientInRecipe',
                to='recipes.ingredient',
                verbose_name='список ингредиентов рецепта',
            ),
        ),
    ]

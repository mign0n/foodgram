from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='ингредиент',
        max_length=100,
    )
    measurement_unit = models.CharField(
        verbose_name='единица измерения',
        max_length=20,
    )

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(
        verbose_name='метка',
        max_length=50,
        unique=True,
    )
    color = models.CharField(
        verbose_name='цвет метки',
        max_length=16,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='слаг',
        max_length=50,
        unique=True,
    )

    def __str__(self) -> str:
        return f'Метка {self.name}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор рецепта',
    )
    cooking_time = models.IntegerField(verbose_name='время приготовления')
    image = models.ImageField(
        verbose_name='фото готового блюда',
        upload_to=settings.IMAGE_PATH,
        null=True,
        default=None,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        verbose_name='список ингредиентов рецепта',
    )
    name = models.CharField(
        verbose_name='название рецепта',
        max_length=200,
    )
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True,
    )
    tags = models.ManyToManyField(Tag, verbose_name='список меток')
    text = models.TextField(verbose_name='описание рецепта')

    class Meta:
        ordering = ('-pub_date',)
        default_related_name = '%(class)s'

    def __str__(self) -> str:
        return f'{self.name} пользователя {self.author}'


class IngredientInRecipe(models.Model):
    amount = models.FloatField(verbose_name='количество ингредиента в рецепте')
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.RESTRICT,
        verbose_name='ингредиент',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='рецепт',
    )

    class Meta:
        default_related_name = '%(class)s'

    def __str__(self) -> str:
        return (
            f'Ингредиент {self.ingredient} в рецепте {self.recipe}; '
            f'количество: {self.amount}'
        )


class Favorite(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='владелец списка избранных рецептов',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='список избранных рецептов',
    )

    class Meta:
        default_related_name = '%(class)s'

    def __str__(self) -> str:
        return (
            f'Рецепт "{self.recipe.name}" в списке избранных '
            f'пользователя {self.owner}'
        )


class Cart(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='владелец списка рецептов для закупки продуктов',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='список рецептов для закупки продуктов',
    )

    class Meta:
        default_related_name = '%(class)s'

    def __str__(self) -> str:
        return (
            f'Рецепт "{self.recipe.name}" в списке покупок '
            f'пользователя {self.owner}'
        )


class Subscribe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь-автор',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='пользователь-подписчик',
    )

    class Meta:
        default_related_name = '%(class)s'

    def __str__(self) -> str:
        return f'{self.user} подписан на {self.author}'

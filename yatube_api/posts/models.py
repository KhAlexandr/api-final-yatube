from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

LENGTH_TEXT = 20


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Сообщество'
    )

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Group(models.Model):
    """Класс для создания сообществ."""

    title = models.CharField(
        max_length=200,
        verbose_name='Название сообщества',
        db_index=True
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='адрес'
    )
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'
        ordering = ('title',)

    def __str__(self):
        return self.title[:LENGTH_TEXT]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Класс для подписки на авторов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('following',)
        constraints = (
            models.UniqueConstraint(
                fields=('following', 'user'),
                name='unique_follow'
            ),
            models.CheckConstraint(
                check=~models.Q(following=models.F('user')),
                name='check_following'
            )
        )

    def __str__(self):
        return f'{self.user} подписан на: {self.following}'[:LENGTH_TEXT]

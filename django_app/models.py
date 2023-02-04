from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,
    )

    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=True,
        db_index=True,
        max_length=150
    )

    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f"Post: {self.title} {self.description[:30]} [{self.id}]"





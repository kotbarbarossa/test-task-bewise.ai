from django.db import models


class Question(models.Model):
    """Quiz question model."""
    id = models.CharField(
        'question id',
        primary_key=True,
        null=False,
        unique=True,
        max_length=20)

    question = models.CharField(
        'question text',
        max_length=500,
        null=False)

    answer = models.CharField(
        'answer text',
        max_length=100,
        null=False)

    created_at = models.DateTimeField(
        'created date'
    )

    date_add = models.DateTimeField(
        'date added',
        auto_now_add=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('-date_add', )

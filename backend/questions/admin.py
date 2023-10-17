from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question admin class."""
    list_display = (
        'id',
        'question',
        'answer',
        'created_at',
        'date_add',)
    search_fields = ('question', 'answer', 'created_at', 'date_add')
    list_filter = ('answer',)

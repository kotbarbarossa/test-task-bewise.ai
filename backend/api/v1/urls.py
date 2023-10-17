from django.urls import path

from .views import QuestionsNumberView

urlpatterns = [
    path(
        'questions-number/',
        QuestionsNumberView.as_view(),
        name='questions_number'),
]

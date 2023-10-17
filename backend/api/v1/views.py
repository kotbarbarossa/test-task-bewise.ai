import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from questions.models import Question

from .serializers import QuestionSerializer, JserviceAPISerializer


class QuestionsNumberView(APIView):
    """Questions view class."""
    @staticmethod
    def get_previous_question():
        try:
            return Question.objects.latest('date_add')
        except Question.DoesNotExist:
            return None

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            num = serializer.validated_data['questions_num']

            previous_question = self.get_previous_question()

            while num > 0:
                try:
                    api_url = f"https://jservice.io/api/random?count={num}"
                    response = requests.get(api_url)
                    response.raise_for_status()
                    data = response.json()
                    serializer = JserviceAPISerializer(data=data, many=True)

                    if serializer.is_valid():
                        serialized_data = serializer.data
                        for item in serialized_data:
                            id = item['id']
                            if not Question.objects.filter(id=id).exists():
                                question = Question(
                                    id=item['id'],
                                    question=item['question'],
                                    answer=item['answer'],
                                    created_at=item['created_at']
                                )
                                question.save()
                                num -= 1

                except requests.exceptions.RequestException:
                    return Response(
                        {'error': 'Ошибка отправки запроса к стороннему API.'},
                        status=500)

            response_data = {
                'result': 'Вопросы успешно сохранены в базе',
                'previous_question': (
                    JserviceAPISerializer(previous_question).data
                    if previous_question else {}
                )
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)

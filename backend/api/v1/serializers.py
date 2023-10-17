from rest_framework import serializers

from questions.models import Question


class PositiveIntegerField(serializers.Field):
    """Custom integer field serializer class."""
    def to_internal_value(self, data):
        try:
            value = int(data)
        except ValueError:
            raise serializers.ValidationError(
                "Значение должно быть положительным целым числом.")

        if value <= 0:
            raise serializers.ValidationError(
                "Значение должно быть положительным целым числом.")

        return value

    def to_representation(self, value):
        return value


class QuestionSerializer(serializers.Serializer):
    """Question serializer class."""
    questions_num = PositiveIntegerField()


class JserviceAPISerializer(serializers.ModelSerializer):
    """External API serializer class."""
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S.%fZ')

    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'answer',
            'created_at',
            )

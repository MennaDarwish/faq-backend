from rest_framework import serializers
from main.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.HyperlinkedIdentityField(many=True, read_only=True,
                                                   view_name='answer-detail')
    tags = serializers.HyperlinkedIdentityField(many=True, read_only=True,
                                                view_name='tag-detail')

    class Meta:
        model = Question
        fields = ('body', 'title', 'attachment', 'tags', 'answers')

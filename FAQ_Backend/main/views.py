from main.models import Question, Tag, Answer
from rest_framework import generics
from main.serializers import (QuestionSerializer,
                              TagSerializer, AnswerSerializer,
                              AutocompleteSerializer)
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackAutocompleteFilter
# from rest_framework import permissions
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'questions': reverse('question-list', request=request, format=format),
        'tags': reverse('tag-list', request=request, format=format),
        'answers': reverse('answer-list', request=request, format=format)
    })


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AutocompleteSearchViewSet(HaystackViewSet):
    index_models = [Question]
    serializer_class = AutocompleteSerializer
    filter_backends = [HaystackAutocompleteFilter]

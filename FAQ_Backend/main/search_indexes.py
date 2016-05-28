from haystack import indexes
from main.models import Question


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(model_attr="id")
    body = indexes.CharField(model_attr='body')
    title = indexes.CharField(model_attr='title')

    autocomplete = indexes.EdgeNgramField(model_attr="title")

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((
            obj.body, obj.title
        ))

    def get_model(self):
        return Question

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

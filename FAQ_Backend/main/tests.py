from rest_framework.test import APITestCase
from main.models import Question, Tag
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.client import RequestFactory
from main.views import QuestionDetail, TagDetail
# Create your tests here.


class QuestionAPITestCase(APITestCase):
    def setUp(self):
        self.question1 = Question.objects.create(body="Question1 body",
                                                 title="Question1 title")
        self.question2 = Question.objects.create(body="Question2 body",
                                                 title="Question2 title")
        Question.objects.get_or_create(body="body3", title="title3")
        self.factory = RequestFactory()

    def test_unicode_representation(self):
        """
        Ensures that the model string representation is equal to 'title'
        """
        question = Question.objects.create(body="Question3 body",
                                           title="Question3 title")
        self.assertEqual(str(question), 'Question3 title')

    def test_list_questions(self):
        """
        Test that we can get a list of questions
        """
        response = self.client.get('/questions/')
        self.assertEqual(response.status_code, 200)
        print "response.data", response.data
        self.assertEqual(response.data[0]['body'],
                         'Question1 body')
        self.assertEqual(response.data[1]['title'],
                         'Question2 title')

    def test_create_question(self):
        """
        Test to ensure a question is created
        """
        attachment = SimpleUploadedFile("file.mp4", "file_content",
                                        content_type="video/mp4")
        response = self.client.post(reverse('question-list'), {
            u"body": "Body1",
            u"title": "title1",
            u"attachment": attachment,
            u"tags": [],
            u"answers": []
        })
        print "response", response
        self.assertEqual(response.status_code, 201)

    def test_detail_view_question(self):
        request = self.factory.get(
            reverse('question-detail', kwargs={"pk": 1}))
        response = QuestionDetail.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)


class TagAPITestCase(APITestCase):
    def setUp(self):
        self.question1 = Question.objects.create(body="Question1 body",
                                                 title="Question1 title")
        self.tag = Tag.objects.create(question=self.question1, name="django")
        self.factory = RequestFactory()

    def test_unicode_representation(self):
        """
        Ensures that the model string representation is equal to 'title'
        """
        self.assertEqual(str(self.tag), 'django')

    def test_list_tags(self):
        """
        Test that we can get a list of questions
        """
        response = self.client.get('/tags/')
        self.assertEqual(response.status_code, 200)
        print "response.data", response.data
        self.assertEqual(response.data[0]['name'],
                         'django')

    def test_create_tag(self):
        """
        Test to ensure a tags is created
        """
        response = self.client.post(reverse('tag-list'), {
            u"question": self.question1.pk,
            u"name": "django",
        })
        print "response", response
        self.assertEqual(response.status_code, 201)

    def test_detail_view_tag(self):
        request = self.factory.get(
            reverse('tag-detail', kwargs={"pk": 1}))
        response = TagDetail.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime


class Question_model_tests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

# learn test later,not finish

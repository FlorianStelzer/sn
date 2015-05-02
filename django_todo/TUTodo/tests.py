from django.core.urlresolvers import reverse

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Todo

# Create your tests here.


def create_todo(title, days_delta, finished):
    deadline = timezone.now() + datetime.timedelta(days=days_delta)
    return Todo.objects.create(title=title, deadline=deadline, finished=finished)


class TodoMethodTests(TestCase):
    def test_index_view(self):
        t1 = create_todo('test1 todo', -100, 0)
        t2 = create_todo('test2 todo', -200, 0)
        t3 = create_todo('test3 todo', 0, 0)
        t4 = create_todo('test4 todo', 100, 43)
        t5 = create_todo('test5 todo', 200, 43)
        response = self.client.get(reverse('TUTodo:index'))
        self.assertContains(response, t1.__str__())
        self.assertContains(response, t2.__str__())
        self.assertContains(response, t3.__str__())
        self.assertContains(response, t4.__str__())
        self.assertContains(response, t5.__str__())
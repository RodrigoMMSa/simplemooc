from django.test import TestCase
from django.core import mail
from django.test.client import Client
from django.urls import reverse
from django.conf import settings

from .models import Course


class ContactCourseTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='django')

    def tearDown(self):
        self.course.delete()

    def test_contact_form_error(self):
        data = {'name': 'Fulano de Tal', 'email': '', 'message': ''}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')

    def test_contact_form_success(self):
        data = {'name': 'Fulano de Tal', 'email': 'rodrigommsa@hotmail.com', 'message': 'teste'}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])

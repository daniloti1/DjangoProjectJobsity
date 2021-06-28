from django.test import TestCase
from .models import *

class ChatTestCase(TestCase):
    def create_chat(self):
        return Chat.objects.create(title='Test Chat')

    def test_chat(self):
        instance = self.create_chat()
        self.assertTrue(isinstance(instance, Chat))

class MessageTestCase(TestCase):
    def create_message(self):
        user = User.objects.create_superuser('admin','test@test.com','admin')
        chat = Chat.objects.create(title='Test Chat')
        return Message.objects.create(user=user, chat=chat, content='Test Message')

    def test_message(self):
        instance = self.create_message()
        self.assertTrue(isinstance(instance, Message))
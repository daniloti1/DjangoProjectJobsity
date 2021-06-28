from django.db import models
from django.contrib.auth.models import User
import datetime

class Chat(models.Model):
	STATES = (( 'A', 'Active' ), ( 'I', 'Inactive' ))
	title = models.CharField(max_length=50)
	state = models.CharField(max_length=1, choices=STATES, default='A')

	registration_date = models.DateTimeField(auto_now_add=True)
	modification_date = models.DateTimeField(auto_now=True, blank=True, null=True)
	registration_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)s_registration_user')
	modification_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)s_modification_user')

	def __str__(self):
		return self.title

class Message(models.Model):
	STATES = (( 'A', 'Active' ), ( 'I', 'Inactive' ))
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chats')
	content = models.CharField(max_length=50)
	state = models.CharField(max_length=1, choices=STATES, default='A')

	registration_date = models.DateTimeField(auto_now_add=True)
	modification_date = models.DateTimeField(auto_now=True, blank=True, null=True)
	registration_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)s_registration_user')
	modification_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)s_modification_user')

	def __str__(self):
		return self.content

from django.contrib.auth.models import User
from main.models import *

admin = User.objects.create_superuser(username='admin', password='admin', first_name='ADMIN', email='test@test.com')
admin.admin_user = True
admin.save()

Chat.objects.create(title='Main Chat', registration_user=admin)

bot = User.objects.create_superuser(username='bot', password='bot', first_name='BOT', email='test@test.com')
bot.admin_user = True
bot.save()
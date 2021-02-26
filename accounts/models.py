from django.contrib.auth.models import User, models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sms = models.CharField(max_length=100)
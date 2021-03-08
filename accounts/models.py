from django.contrib.auth.models import User, models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sms = models.CharField(max_length=100)

class FriendsGroup(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    host = models.ForeignKey(User, related_name='hosts', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.name

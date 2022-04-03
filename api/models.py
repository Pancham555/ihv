from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class Feedback(models.Model):
    feedback_email_asker = models.CharField(max_length=100)
    feedback_question = models.CharField(primary_key=True, max_length=100)
    feedback_answer = models.CharField(max_length=100)
    feedback_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback_question


# make a comment class where there will be an another class of reply in the form of an array
class Comment(models.Model):
    # set max length to infinity in charfield
    comment = models.CharField(max_length=1000)
    comment_maker = models.CharField(max_length=100, default='')
    comment_date = models.DateTimeField(auto_now_add=True)
    # comment_feedback = models.ForeignKey(
    #     'auth.user', related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

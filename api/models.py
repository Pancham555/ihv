from django.db import models
# # Create your models here.
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q
from django.contrib.auth.models import User


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:  # to allow authentication through phone number or any other field, modify the below statement
            user = UserModel.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None


class Feedback(models.Model):
    feedback_username = models.CharField(max_length=100)
    feedback_question = models.CharField(primary_key=True, max_length=100)
    feedback_answer = models.CharField(max_length=100, null=True, default=None)
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


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

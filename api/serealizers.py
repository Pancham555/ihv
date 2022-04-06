'''Serealize models here'''
# from django.forms import CharField, ValidationError
from rest_framework import serializers
from .models import Feedback, Comment
from rest_framework_simplejwt.serializers import TokenObtainSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# import PasswordField


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('__all__')

        def create(self, validated_data, **kwargs):
            return Feedback.objects.create(**validated_data, **kwargs)

        def update(self, instance, validated_data):
            instance.feedback_username = validated_data.get(
                'feedback_username', instance.feedback_username)
            instance.feedback_question = validated_data.get(
                'feedback_question', instance.feedback_question)
            instance.feedback_answer = validated_data.get(
                'feedback_answer', instance.feedback_answer)
            instance.save()
            return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("__all__")


# class EmailTokenObtainSerializer(TokenObtainSerializer):
#     # username_field = User.EMAIL_FIELD
#     pass

    # email = serializers.EmailField(required=True)

    # def __init__(self, *args, **kwargs):
    #     super(EmailTokenObtainSerializer, self).__init__(*args, **kwargs)

    #     self.fields[self.username_field] = CharField()
    #     self.fields['password'] = CharField()

    # def validate(self, attrs):
    #     # self.user = authenticate(**{
    #     #     self.username_field: attrs[self.username_field],
    #     #     'password': attrs['password'],
    #     # })
    #     self.user = User.objects.filter(
    #         email=attrs[self.username_field]).first()
    #     print(self.user)

    #     if not self.user:
    #         raise ValidationError('The user is not valid.')

    #     if self.user:
    #         if not self.user.check_password(attrs['password']):
    #             raise ValidationError('Incorrect credentials.')
    #     print(self.user)
    #     # Prior to Django 1.10, inactive users could be authenticated with the
    #     # default `ModelBackend`.  As of Django 1.10, the `ModelBackend`
    #     # prevents inactive users from authenticating.  App designers can still
    #     # allow inactive users to authenticate by opting for the new
    #     # `AllowAllUsersModelBackend`.  However, we explicitly prevent inactive
    #     # users from authenticating to enforce a reasonable policy and provide
    #     # sensible backwards compatibility with older Django versions.
    #     if self.user is None or not self.user.is_active:
    #         raise ValidationError(
    #             'No active account found with the given credentials')

    #     return {}

    # @classmethod
    # def get_token(cls, user):
    #     raise NotImplemented(
    #         'Must implement `get_token` method for `MyTokenObtainSerializer` subclasses')


# class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
#     @classmethod
#     def get_token(cls, user):
#         return RefreshToken.for_user(user)

#     def validate(self, attrs):
#         data = super().validate(attrs)

#         refresh = self.get_token(self.user)

#         data["refresh"] = str(refresh)
#         data["access"] = str(refresh.access_token)

#         return data


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

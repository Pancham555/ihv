'''Serealize models here'''
from rest_framework import serializers
from .models import Feedback, Comment


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('feedback_email_asker',
                  'feedback_question', 'feedback_answer')

        def create(self, validated_data, **kwargs):
            return Feedback.objects.create(**validated_data, **kwargs)

        def update(self, instance, validated_data):
            instance.feedback_email_asker = validated_data.get(
                'feedback_email_asker', instance.feedback_email_asker)
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

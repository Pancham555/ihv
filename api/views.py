import re
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from api.models import Comment, Feedback
from api.serealizers import CommentSerializer, FeedbackSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
# from rest_framework import renderers, parsers
# from rest_framework.authtoken.views import APIView
# from rest_framework.authtoken import views as auth_views
# from rest_framework.compat import coreapi, coreschema
# from rest_framework.schemas import ManualSchema


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def logoutuser(req):
    try:
        user = authenticate(email=req.data.get('email'),
                            password=req.data.get('password'))
        print(user, "User")
        if user is not None:
            print(user, "User")
            logout(req)
    except Exception as e:
        print(e)
    return Response({'message': "Logout Successful"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(req):
    data = req.data
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    if password is not None and email is not None and username is not None:
        try:
            user = User(username=username,
                        email=email,
                        password=make_password(password))
            user.save()
            token = RefreshToken.for_user(user)
            return Response({
                'message': "Signup Successful",
                'access': str(token.access_token),
                'refresh': str(token)
            })
        except Exception as e:
            print(e)
            return Response({'message': "Signup Failed"})


# Feedback
@login_required
@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def feedback(req):
    if req.method == 'POST':
        if req.user.is_superuser and not req.data.get('question'):
            try:
                data = req.data
                FeedbackSerializer().update(
                    instance=Feedback.objects.get(
                        'feedback_question', req.data.get('question')),
                    validated_data=data,)
                # Feedback.objects.filter(
                #     feedback_email_asker=data.get('email')).all().update(
                #     feedback_answer=data.get('answer'))
            except Exception as e:
                print(e, "This is the problem")
            return Response({'message': 'YOU ARE A SUPERUSER'})

        else:
            data = req.data
            FeedbackSerializer(data=data).save()
            return Response({'message': 'Feedback done'})
    else:
        data = FeedbackSerializer(Feedback.objects.all(), many=True)
        return Response(data.data)


@permission_classes((permissions.IsAuthenticated,))
@api_view(['GET', 'POST'])
def comment(req):
    # return Response({'message': 'Comment'})
    if req.method == 'POST':
        data = req.data
        savedata = Comment(comment=data.get('comment'),
                           comment_maker=req.user.username)
        print(data, "data")
        savedata.save()
        return Response({'message': 'Comment done'})
    else:
        data = CommentSerializer(Comment.objects.all(), many=True)
        return Response(data.data)
    # return Response({'message': 'Comment done'})

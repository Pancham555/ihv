from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout
from api.models import Comment, Feedback
from api.serealizers import CommentSerializer,  FeedbackSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def index(req):
    print('Someone entered here')
    return Response({'message': 'Credential Correct!'})


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


@ api_view(['GET', 'POST'])
@ permission_classes((permissions.IsAuthenticated,))
def feedback(req):
    if req.method == 'POST':
        if req.user.is_superuser and req.data.get('feedback_question') and req.data.get('feedback_answer'):
            try:
                data = req.data
                # FeedbackSerializer().update(
                #     instance=Feedback.objects.get(
                #         'feedback_question', req.data.get('question')),
                #     validated_data=data,)
                Feedback.objects.filter(
                    feedback_question=data.get('feedback_question')).all().update(
                    feedback_answer=data.get('feedback_answer'))
            except Exception as e:
                print(e, "This is the problem")
            return Response({'message': 'Question answered. Superuser!'})

        else:
            data = req.data
            # FeedbackSerializer(feedback_question=data.get('feedback_question'),
            #                    feedback_answer=data.get('feedback_answer'),
            #                    feedback_email_asker=req.user.email).is_valid(
            #     raise_exception=True)
            Feedback(feedback_question=data.get('feedback_question'),
                     feedback_email_asker=req.user.email).save()
            return Response({'message': 'Feedback done'})
    else:
        data = FeedbackSerializer(Feedback.objects.all(), many=True)
        return Response(data.data)


@ permission_classes((permissions.IsAuthenticated,))
@ api_view(['GET', 'POST'])
def comment(req):
    if req.method == 'POST':
        try:
            data = req.data
            savedata = Comment(comment=data.get('comment'),
                               comment_maker=req.user.username or req.user.email)
            savedata.save()
            return Response({'message': 'Comment done'})
        except Exception as e:
            print("Problem", e)
            return Response({'message': 'Something went wrong'})
    else:
        data = CommentSerializer(Comment.objects.all(), many=True)
        res = Response(data.data)
        return res

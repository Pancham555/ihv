from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
# set csrf token when get method is called
# import login from rest


@ensure_csrf_cookie
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def index(request):
    if request.method == 'GET':
        res = Response({'message': 'Hello, world!'})
        res.csrf_cookie_set = True
        return res
    else:
        email = request.data.get('email')
        password = request.data.get('password')

        res = Response({'email': email, 'password': password})
        res.csrf_cookie_set = True
        res.set_cookie('fs', "fs")
        return res

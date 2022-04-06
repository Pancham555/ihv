from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
# set csrf token when get method is called
# import login from rest


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def index(req):
    return Response({'message': 'Hello, World!'})

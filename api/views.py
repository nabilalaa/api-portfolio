from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def about(request):

    about = About.objects.all()
    serializer = AboutSerializer(about, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project(request):

    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
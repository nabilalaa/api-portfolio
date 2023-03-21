from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serailzers import *


@api_view(['GET'])
def about(request):

    about = About.objects.all()
    serailzers = AboutSerializer(about, many=True)
    return Response(serailzers.data)

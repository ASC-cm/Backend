from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User

@api_view(["POST"])
def submit_form(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully", "data": serializer.data}, status=201)
    return Response(serializer.errors, status=400)


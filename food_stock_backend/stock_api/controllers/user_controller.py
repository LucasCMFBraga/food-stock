from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from stock_api.serializers.user_serializer import UserSerializer

class UserController(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer =  UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages
            },
            status = status.HTTP_400_BAD_REQUEST
        )
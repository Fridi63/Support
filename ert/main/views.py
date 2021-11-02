import django
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, generics, status
from .serializers import SupportSerializer
from .models import Support
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import send_email
from .serializers import CreateUser
from django.contrib.auth.models import User
django.contrib.auth.hashers


# # for Support model
# class UserView(APIView):
#
#     def get(self, request):
#
#         supports = Support.objects.all()
#         users = User.objects.all()
#         serializer = SupportSerializer(many=True)
#         return Response(serializer.data)


class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        content = {
            'user': str(request.user),
        }
        return Response(content)


class CreateUserView(APIView):
    def post(self, request):
        serializer = CreateUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        username, password, email = serializer.data.values()

        # try:
        #     User.objects.get(username)
        # except ObjectDoesNotExist:
        #     return Response(data="user already exist", status=status.HTTP_400_BAD_REQUEST)

        u = User(username=username, password=password, email=email)
        u.set_password(password)
        u.save()

        send_email("Registration", "Follow this link:", 'admin@gmail.com', email)

        return Response(data="User was successfully created.", status=status.HTTP_201_CREATED)

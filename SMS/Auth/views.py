from django.contrib.auth import authenticate
from rest_framework import generics, views
from .serializers import User, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)

            return Response(
                data={'details':f'welcome {user.username} !!!'}
            )
        else:
            return Response({'error': 'Invalid credentials.'}, status=400)


class LogoutView(views.APIView):

    def post(self,request):

        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(data={'details':'logout successfully !!!'},status=status.HTTP_200_OK)

        except Exception as E:
            print(E)
            return Response(status=status.HTTP_400_BAD_REQUEST)
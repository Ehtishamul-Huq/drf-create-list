from django.shortcuts import render
from .models import User
from .serializers import UserSerializer 
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class UserView(generics.CreateAPIView): 
    serializer_class=UserSerializer 
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()     
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)


class UserListView(generics.ListAPIView):
    serializer_class=UserSerializer 
    queryset = User.objects.all()

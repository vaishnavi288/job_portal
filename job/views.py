from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from job.serializers import jobserializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from  job.permissions import IsJobOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from job.models import job
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class Register(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response (serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)




class create(APIView):
    permission_classes=[IsJobOwnerOrReadOnly]
    authentication_classes=[TokenAuthentication]
    def post(self,request):

        form_data=request.data
        serializer_insatnce=jobserializer(data=form_data)
        if serializer_insatnce.is_valid():
            serializer_insatnce.save(posted_by=request.user)
            return Response (serializer_insatnce.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_insatnce.errors,status=status.HTTP_400_BAD_REQUEST)


class view(APIView):
    permission_classes=[IsJobOwnerOrReadOnly]
    def get(self,request):
        j=job.objects.all()
        serializer_instance=jobserializer(j,many=True)
        return Response (serializer_instance.data,status=status.HTTP_200_OK)


class retrive(APIView):
    permission_classes=[IsJobOwnerOrReadOnly]
    def get(self,request,i):
        j=get_object_or_404(job,id=i)
        self.check_object_permissions(request,j)
        serializer_instance=jobserializer(j)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
class update(APIView):
    permission_classes=[IsJobOwnerOrReadOnly]
    authentication_classes=[TokenAuthentication]
    def put(self,request,i):
        j=get_object_or_404(job,id=i)
        self.check_object_permissions(request,j)
        serializer_instance=jobserializer(j,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response (serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class delete(APIView):
    permission_classes=[IsJobOwnerOrReadOnly]
    authentication_classes=[TokenAuthentication]
    def delete(self,request,i):
        j=get_object_or_404(job,id=i)
        self.check_object_permissions(request,j)
        j.delete()
        return Response ("deleted")


class Logout(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        
        print(self.request.user)
        self.request.user.auth_token.delete()
        return Response({"message":"logout succesfuly"})

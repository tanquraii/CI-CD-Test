from django.shortcuts import render
from .serializers import CatUserSerializer,CatUserDetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import CatUser
from django.http import HttpResponse
from django.http import Http404
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

#test something dude
#OO AA OO AA

class ListCreateAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = None
    serializer_class = None

    def get(self,request):
        items = self.queryset.all()#this is custom manager I guess
        serializer = self.serializer_class(items,many=True)
        if items:
            return Response(serializer.data)
        else:
            return HttpResponse('No items found')
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DetailsDeleteAPIView(APIView):
    queryset = None
    serializer_class = None

    def get_object(self, id):#this function just gets the object
        try:
            return self.queryset.get(id=id)
        except self.queryset.model.DoesNotExist:
            raise Http404

    def get(self, request, id):
        item = self.get_object(id)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def delete(self, request, id):
        item = self.get_object(id)
        item.delete()
        return Response({'detail': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def put(self,request,id):
        item = self.get_object(id)
        serializer = self.serializer_class(item,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'detail':'Serializer is not valId'},status = status.HTTP_400_BAD_REQUEST)

class CatUserView(ListCreateAPIView):
    queryset = CatUser.objects.all()
    serializer_class = CatUserSerializer

class CatUserDetailsView(DetailsDeleteAPIView):
    queryset = CatUser.objects.all()
    serializer_class = CatUserDetailsSerializer
# Create your views here.

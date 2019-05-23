from autos.models import Auto
from .serializers import AutoSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import JSONParser

# Create your views here.
class AutoList(APIView):
    queryset = Auto.objects.all()
    def get(self,request,format=None):
       queryset = Auto.objects.all()
       serializer = AutoSerializer(queryset,many=True)
       return Response(serializer.data)

    def post(self, request, format = None):
       serializer = AutoSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           datas = serializer.data
           response = datas
           return Response(response,status=status.HTTP_201_CREATED)  
       response = serializer.errors
       return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        data = request.data
        auto = Auto.objects.get(id=pk)
        serializer = AutoSerializer(auto, data=data)
        if serializer.is_valid():
            autoUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk,format=None):
        # Get object with this pk
        auto = get_object_or_404(Auto.objects.all(), pk=pk)
        auto.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204) 
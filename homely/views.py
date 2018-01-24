from django.shortcuts import render

# Create your views here.
from homely.models import PropertyDetails,HomeOwnerAccount
from homely.serializers import (PropertyDetailSerializer,
	HomeOwnerAccountSerializer,HomeOwnerSerializer,UserSerializer)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
def index(request):
	return render(request,'homely/index.html')
class UserDetails(APIView):
    def get(self,request):
        owner_details = User.objects.all()
        serializer = UserSerializer(owner_details, many=True)
        return Response(serializer.data)

class OwnerDetails(APIView):
    def get_object(self, pk):
        try:
            return HomeOwnerAccount.objects.get(pk=pk)
        except PropertyDetails.DoesNotExist:
            raise Http404
    def get(self,request):
        owner_details = HomeOwnerAccount.objects.all()
        serializer = HomeOwnerSerializer(owner_details, many=True)
        return Response(serializer.data)
    def post(self, request):#, format=None):
    	# import ipdb
    	# ipdb.set_trace()
        serializer = HomeOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print serializer.data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        owner_details = self.get_object(pk)
        serializer = HomeOwnerSerializer(owner_details,read_only=False, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):#, format=None):
        owner_details = self.get_object(pk)
        owner_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PropertyDetailsList(APIView):
    def get_object(self, pk):
        try:
            return PropertyDetails.objects.get(pk=pk)
        except PropertyDetails.DoesNotExist:
            raise Http404
    def get(self,request):
        property_details = PropertyDetails.objects.all()
        serializer = PropertyDetailSerializer(property_details, many=True)
        return Response(serializer.data)
    def post(self, request):#, format=None):
    	# import ipdb
    	# ipdb.set_trace()
        serializer = PropertyDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print serializer.data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
    	import ipdb
    	ipdb.set_trace()
        property_details = self.get_object(pk)
        serializer = PropertyDetailSerializer(
        	property_details,read_only=False, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):#, format=None):
        owner_details = self.get_object(pk)
        owner_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class OwnerPropertyDetailsList(APIView):
    def get(self, request):#, format=None):
        owner_property_details = HomeOwnerAccount.objects.all()
        serializer = HomeOwnerAccountSerializer(owner_property_details, many=True)
        return Response(serializer.data)

    def post(self, request):#, format=None):
    	# import ipdb
    	# ipdb.set_trace()
        serializer = HomeOwnerAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print serializer.data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UDOwnerPropertyDetailList(APIView):
    def put(self,request,owner_id):
    	# import ipdb
    	# ipdb.set_trace()
        try:
            owner = HomeOwnerAccount.aobjects.get(pk=owner_id)
        except HomeOwnerAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = HomeOwnerAccountSerializer(owner, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PropertyDetailsList(APIView):
    """
    List all PropertyDetails, or create a new snippet.
    """
    def get(self, request):#, format=None):
        PropertyDetails_obj = PropertyDetails.objects.all()
        serializer = PropertyDetailSerializer(PropertyDetails_obj, many=True)
        return Response(serializer.data)

    def post(self, request):#, format=None):
        serializer = PropertyDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return PropertyDetails.objects.get(pk=pk)
        except PropertyDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk):#, format=None):
        PropertyDetail = self.get_object(pk)
        serializer = PropertyDetailSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):#:, format=None):
        PropertyDetail = self.get_object(pk)
        serializer = PropertyDetailSerializer(PropertyDetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):#, format=None):
        PropertyDetail = self.get_object(pk)
        PropertyDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
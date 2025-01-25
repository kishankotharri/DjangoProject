from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from loginify_app.models import UserDetail
from loginify_app.serializers import UserDetailSerializer

# for API
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

import json

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_data(request):
    if request.method == 'GET':
        try:
            all_users = UserDetail.objects.all()
            serializer_data = UserDetailSerializer(all_users, many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except UserDetail.DoesNotExist:
                return JsonResponse({"error": "Users not found."}, status=404)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_data_by_username(request, username):
    if request.method == 'GET':
        try:
            user = UserDetail.objects.get(username=username)
            serializer_data = UserDetailSerializer(user)
            return JsonResponse(serializer_data.data, safe=False)
        except UserDetail.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_data(request):
    if request.method == 'POST':
        serializer_data = UserDetailSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data, safe=False)
        return JsonResponse({"error": "Somthing wrong."}, status=404)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_data_by_username(request, username):
    if request.method == 'PUT':
        try:
            user = UserDetail.objects.get(username=username)
            serializer_data = UserDetailSerializer(user, data=request.data, partial=True)
            
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse(serializer_data.data, safe=False, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except UserDetail.DoesNotExist:
            return JsonResponse({"error": "User not found."}, status=404)
        
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_data_by_username(request, username):
    try:
        user = UserDetail.objects.get(username=username)
        user.delete()
        return JsonResponse({"message": "User deleted."}, status=200)
    except UserDetail.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)
from django.shortcuts import render
 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Prompt, PromptDetail
import csv
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10  # Specify the number of items per page
    page_size_query_param = 'page_size'  # Customize the query parameter for page size
    max_page_size = 100  # Optionally specify the maximum page size
@api_view(['POST'])
def upload_prompts(request):
    if request.method == 'POST' and request.FILES.get('file'):
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return JsonResponse({'error': 'File must be a CSV'}, status=400)
        
        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                Prompt.objects.create(content=row['content'], category=row['category'])
            
            return JsonResponse({'message': 'Prompts uploaded successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'File not provided'}, status=400)

@api_view(['POST'])
def upload_prompt_details(request):
    if request.method == 'POST' and request.FILES.get('file'):
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return JsonResponse({'error': 'File must be a CSV'}, status=400)
        

from rest_framework import generics 
from .serializers import PromptSerializer, PromptDetailSerializer

class PromptListCreate(generics.ListCreateAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    pagination_class = CustomPagination

class PromptDetailCreate(generics.CreateAPIView):
    queryset = PromptDetail.objects.all()
    serializer_class = PromptDetailSerializer

class PromptDetailListCreate(generics.ListCreateAPIView):
    queryset = PromptDetail.objects.all()
    serializer_class = PromptDetailSerializer
    pagination_class = CustomPagination
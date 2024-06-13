"""prompts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ai_prompts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bulk-upload/', views.upload_prompts, name='bulk-upload'),
    path('bulk-upload-details/',views.upload_prompt_details,name='bulk-upload-details'),
    path('api/prompts/', views.PromptListCreate.as_view(), name='prompt-list-create'),
    path('api/prompts/<int:pk>/', views.PromptDetailCreate.as_view(), name='prompt-detail-create'),
    path('api/prompt-details/', views.PromptDetailListCreate.as_view(), name='prompt-detail-list-create'),
]

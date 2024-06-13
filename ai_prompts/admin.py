from django.contrib import admin

from ai_prompts.models import Prompt, PromptDetail

# Register your models here.
admin.site.register(Prompt)
admin.site.register(PromptDetail)
from django.db import models

class Prompt(models.Model):
    content = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.content

class PromptDetail(models.Model):
    element = models.CharField(max_length=255)
     
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE ,related_name='details')

    def __str__(self):
        return self.content
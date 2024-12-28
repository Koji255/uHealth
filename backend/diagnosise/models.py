from django.db import models

from users.models import User

# Create your models here.
class Diagnosis(models.Model):

    symptoms = models.CharField(max_length=250, blank=False, null=False,
                                verbose_name='Symptoms')
    
    disease_category = models.CharField(max_length=250,
                                        verbose_name='Disease Category')
    
    description = models.TextField(editable=False, 
                                   verbose_name='AI Explanation')
    
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Date Created')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'user_id: {self.user}, disease_category: {self.disease_category}'
    

    class Meta:
        verbose_name = "AI's Diagnosis"
        verbose_name_plural = "AI's Diagnoses"
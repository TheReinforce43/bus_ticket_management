from django.db import models 

from support_function.division_list import division_list 
from user.models import User 



class ServiceDistrictModel(models.Model):

    division = models.CharField(max_length=50, choices=division_list)
    districtName = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    responsiblePerson = models.ForeignKey(User, on_delete=models.CASCADE,related_name='responsible_person',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.districtName
    
    class Meta:
        db_table = 'ServiceDistrictModel'
        verbose_name = 'Service District'
        verbose_name_plural = 'Service Districts'
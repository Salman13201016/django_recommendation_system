from django.db import models
from category.models import categories

class courses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    cat_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    description = models.TextField()
    fee = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to ="images/")
    module = models.TextField()
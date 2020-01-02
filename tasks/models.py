from django.db import models

# Create your models here.
class ToDo(models.Model):
    sr_no =models.AutoField(primary_key=True)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,blank =True)

    def __str__(self):
        return self.content


from django.db import models

# Create your models here.

# chooices = {
#     ('start', 'start'),
#     ('in proces', 'in proces'),
#     ('end', 'end')
# }



class Plane(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


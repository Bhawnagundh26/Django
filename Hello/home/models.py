from django.db import models

#makemigration - create changes and store in a file
#migrate - apply the pending chages created by makemigrations
# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=122)
    email = models.CharField(max_length=123)
    phone =models.charField(max_field=12)
    desc = models.TextField() 
    date = models.Datefield()

    def __str__(self):
        return self.name

from django.db import models
import mptt
from mptt.models import MPTTModel, TreeForeignKey


class Staffmodels(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    position = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=100, decimal_places=2)
    salary_all = models.DecimalField(max_digits=100, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    date_employment = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' Name: ' + self.name

    class Meta:
        ordering = ['name']

    class MPTTMeta:
        order_insertion_py = ['name']


mptt.register(Staffmodels, order_insertion_py=['name'])



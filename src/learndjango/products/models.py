from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # Max length is required for charField
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse("product:product-profile", kwargs={"product_id": self.id})
from django.db import models


class ProductDetail(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class APILog(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    request_body = models.TextField(blank=True, null=True)
    response_body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.method} {self.path}'
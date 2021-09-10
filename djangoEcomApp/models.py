from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    user_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.IntegerField(null=False, blank=False)

            def __str__(self):
        return f"{self.name}, {self.email}, {self.telefone}"

        class Meta:
        verbose_name_plural = "Clientes"
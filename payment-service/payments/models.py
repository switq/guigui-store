from django.db import models


class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending"
        APPROVED = "approved"
        REJECTED = "rejected"
        REFUNDED = "refunded"

    class Method(models.TextChoices):
        CREDIT_CARD = "credit_card"
        PIX = "pix"
        BOLETO = "boleto"

    order_id = models.UUIDField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=Method.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.id} — {self.status}"

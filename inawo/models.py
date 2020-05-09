from django.db import models
from users.models import CustomUser
from django.utils import timezone

# Create your models here.


ACCOUNT_TYPE= (
    ('savings', 'savings'),
    ('current', 'current'),
)

TRANSACTION_TYPE= (
    ('income', 'income'),
    ('expense', 'expense'),
)

CATEGORY_TYPE = (
    ('bank', 'bank'),
    ('cash', 'cash'),
)


class Account(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    current_balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(default=timezone.now, null=False)
    category = models.CharField(default='savings', choices=ACCOUNT_TYPE, max_length=20)

    def __str__(self):
        return self.user.email

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    transaction_type = models.CharField(default='income', choices=TRANSACTION_TYPE,max_length=20)
    amount = models.CharField(default='',max_length=1024)
    payee = models.CharField(max_length=200)
    category = models.CharField(default='bank', choices=CATEGORY_TYPE,max_length=20)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.user.email

class Budget(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.CharField(default='',max_length=1024)
    category = models.CharField(default='bank', choices=CATEGORY_TYPE,max_length=20)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.user.email


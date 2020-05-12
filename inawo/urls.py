from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter


app_name = "home"

urlpatterns = [
    path('transaction/list/<int:account_id>', ListTransaction, name='list_transaction'),
    path('transaction/create/', Transactions, name='createtransaction'),
    path('transaction/edit/<int:transaction_id>', UpdateTransaction, name='edittransaction'),
    path('transaction/deleted/<int:transaction_id>', DeleteTransaction, name='deletetransaction'),
    path('account/create/', CreateAccount, name='createaccount'),
    path('account/edit/<int:account_id>', EditAccount, name='editaccount'),
    path('account/month/<int:account_id>', MonthAccount, name='account_details'),
    path('budget/create/', Budget, name='createbudget'),
    path('budget/edit/<int:budget_id>', EditBudget, name='editbudget'),
    path('budget/delete/<int:budget_id>', DeleteBudget, name='deletebudget'),
    path('v1/dashboard/home/', home, name='home'),
]
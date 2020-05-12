from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from .models import *
from .serializers import * 
from django.core.serializers import serialize 
import json

"""
Dashboard endpoint, to get all
"""
class Dashboard(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        wallets = Account.objects.filter(user=request.user)
        no_of_wallet = Account.objects.filter(user=request.user).count()
        wallets = AccountSerializer(wallets,many=True)



        year_income = {
            'January': 0,
            'February': 0,
            'March': 0,
            'April': 0,
            'May': 0,
            'June': 0,
            'July': 0,
            'August': 0,
            'September': 0,
            'October': 0,
            'November': 0,
            'December': 0,
        }


        year_expense = {
            'January': 0,
            'February': 0,
            'March': 0,
            'April': 0,
            'May': 0,
            'June': 0,
            'July': 0,
            'August': 0,
            'September': 0,
            'October': 0,
            'November': 0,
            'December': 0,
        }

        current_month_earn = 0
        year_trans = Transaction.objects.filter(user=request.user,updated_at__year=datetime.now().year)
        current_month_trans = Transaction.objects.filter(user=request.user,updated_at__year=datetime.now().year,updated_at__month=datetime.now().month)
        
        for trans in current_month_trans:
            if trans.transaction_type == "income":
                current_month_earn += int(trans.amount)
            else:
                current_month_earn -= int(trans.amount)
        for trans in year_trans:
            if trans.updated_at.month == 1:
                if trans.transaction_type == "income":
                    year_income['January'] += int(trans.amount)
                else:
                    year_expense['January'] += int(trans.amount)
            elif trans.updated_at.month == 2:
                if trans.transaction_type == "income":
                    year_income['February'] += int(trans.amount)
                else:
                    year_expense['February'] += int(trans.amount)
            elif trans.updated_at.month == 3:
                if trans.transaction_type == "income":
                    year_income['March'] += int(trans.amount)
                else:
                    year_expense['March'] += int(trans.amount)
            elif trans.updated_at.month == 4:
                if trans.transaction_type == "income":
                    year_income['April'] += int(trans.amount)
                else:
                    year_expense['April'] += int(trans.amount)
            elif trans.updated_at.month == 5:
                if trans.transaction_type == "income":
                    year_income['May'] += int(trans.amount)
                else:
                    year_expense['May'] += int(trans.amount)
            elif trans.updated_at.month == 6:
                if trans.transaction_type == "income":
                    year_income['June'] += int(trans.amount)
                else:
                    year_expense['June'] += int(trans.amount)
            elif trans.updated_at.month == 7:
                if trans.transaction_type == "income":
                    year_income['July'] += int(trans.amount)
                else:
                    year_expense['July'] += int(trans.amount)
            elif trans.updated_at.month == 8:
                if trans.transaction_type == "income":
                    year_income['August'] += int(trans.amount)
                else:
                    year_expense['August'] += int(trans.amount)
            elif trans.updated_at.month == 9:
                if trans.transaction_type == "income":
                    year_income['September'] += int(trans.amount)
                else:
                    year_expense['September'] += int(trans.amount)
            elif trans.updated_at.month == 10:
                if trans.transaction_type == "income":
                    year_income['October'] += int(trans.amount)
                else:
                    year_expense['October'] += int(trans.amount)
            elif trans.updated_at.month == 11:
                if trans.transaction_type == "income":
                    year_income['November'] += int(trans.amount)
                else:
                    year_expense['November'] += int(trans.amount)
            elif trans.updated_at.month == 12:
                if trans.transaction_type == "income":
                    year_income['December'] += int(trans.amount)
                else:
                    year_expense['December'] += int(trans.amount)
        
        
        year_expense = json.dumps(year_expense)
        year_income = json.dumps(year_income)
        trans = Transaction.objects.filter(user=request.user, updated_at__year=datetime.now().year)
        earnings_month = 0
        earnings_annual = 0
        for tran in trans:
            if tran.transaction_type == "income":
                earnings_annual += int(tran.amount)
            else:
                earnings_annual -= int(tran.amount)

        content = {
            'message': 'success',
            'error':False,
            'wallets': wallets.data,
            'no_of_wallet': no_of_wallet,
            'status':status.HTTP_200_OK,
            'annual_earnings': earnings_annual,
            'year_income': year_income,
            'year_expense': year_expense,
            'current_month_earning': current_month_earn
        }
        return Response(content)


"""
Dashboard endpoint, to get all
"""
class Dashboard2(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        wallets = Account.objects.filter(user=request.user)
        no_of_wallet = Account.objects.filter(user=request.user).count()
        wallets = AccountSerializer(wallets,many=True)



        year_income = {
            'January': 0,
            'February': 0,
            'March': 0,
            'April': 0,
            'May': 0,
            'June': 0,
            'July': 0,
            'August': 0,
            'September': 0,
            'October': 0,
            'November': 0,
            'December': 0,
        }


        year_expense = {
            'January': 0,
            'February': 0,
            'March': 0,
            'April': 0,
            'May': 0,
            'June': 0,
            'July': 0,
            'August': 0,
            'September': 0,
            'October': 0,
            'November': 0,
            'December': 0,
        }

        current_month_earn = 0
        year_trans = Transaction.objects.filter(user=request.user,updated_at__year=datetime.now().year)
        current_month_trans = Transaction.objects.filter(user=request.user,updated_at__year=datetime.now().year,updated_at__month=datetime.now().month)
        
        for trans in current_month_trans:
            if trans.transaction_type == "income":
                current_month_earn += int(trans.amount)
            else:
                current_month_earn -= int(trans.amount)
        for trans in year_trans:
            if trans.updated_at.month == 1:
                if trans.transaction_type == "income":
                    year_income['January'] += int(trans.amount)
                else:
                    year_expense['January'] += int(trans.amount)
            elif trans.updated_at.month == 2:
                if trans.transaction_type == "income":
                    year_income['February'] += int(trans.amount)
                else:
                    year_expense['February'] += int(trans.amount)
            elif trans.updated_at.month == 3:
                if trans.transaction_type == "income":
                    year_income['March'] += int(trans.amount)
                else:
                    year_expense['March'] += int(trans.amount)
            elif trans.updated_at.month == 4:
                if trans.transaction_type == "income":
                    year_income['April'] += int(trans.amount)
                else:
                    year_expense['April'] += int(trans.amount)
            elif trans.updated_at.month == 5:
                if trans.transaction_type == "income":
                    year_income['May'] += int(trans.amount)
                else:
                    year_expense['May'] += int(trans.amount)
            elif trans.updated_at.month == 6:
                if trans.transaction_type == "income":
                    year_income['June'] += int(trans.amount)
                else:
                    year_expense['June'] += int(trans.amount)
            elif trans.updated_at.month == 7:
                if trans.transaction_type == "income":
                    year_income['July'] += int(trans.amount)
                else:
                    year_expense['July'] += int(trans.amount)
            elif trans.updated_at.month == 8:
                if trans.transaction_type == "income":
                    year_income['August'] += int(trans.amount)
                else:
                    year_expense['August'] += int(trans.amount)
            elif trans.updated_at.month == 9:
                if trans.transaction_type == "income":
                    year_income['September'] += int(trans.amount)
                else:
                    year_expense['September'] += int(trans.amount)
            elif trans.updated_at.month == 10:
                if trans.transaction_type == "income":
                    year_income['October'] += int(trans.amount)
                else:
                    year_expense['October'] += int(trans.amount)
            elif trans.updated_at.month == 11:
                if trans.transaction_type == "income":
                    year_income['November'] += int(trans.amount)
                else:
                    year_expense['November'] += int(trans.amount)
            elif trans.updated_at.month == 12:
                if trans.transaction_type == "income":
                    year_income['December'] += int(trans.amount)
                else:
                    year_expense['December'] += int(trans.amount)
        
        
        year_expense = json.dumps(year_expense)
        year_income = json.dumps(year_income)
        trans = Transaction.objects.filter(user=request.user, updated_at__year=datetime.now().year)
        earnings_month = 0
        earnings_annual = 0
        for tran in trans:
            if tran.transaction_type == "income":
                earnings_annual += int(tran.amount)
            else:
                earnings_annual -= int(tran.amount)

        content = {
            'message': 'success',
            'error':False,
            'wallets': wallets.data,
            'no_of_wallet': no_of_wallet,
            'status':status.HTTP_200_OK,
            'annual_earnings': earnings_annual,
            'year_income': year_income,
            'year_expense': year_expense,
            'current_month_earning': current_month_earn
        }
        return Response(content)


"""
Get income and expense for a account in current month
"""
@api_view(['GET'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def MonthAccount(request, account_id):
    income=0
    expense=0
    try:
        account = Account.objects.get(id=account_id)
        transaction = Transaction.objects.filter(user=request.user, account=account, updated_at__year=datetime.now().year,updated_at__month=datetime.now().month)

        for trans in transaction:
            if trans.transaction_type == "income":
                income += int(trans.amount)
            else:
                expense += int(trans.amount)
        return JsonResponse({'income':income,'expense':expense,'error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return JsonResponse({'message': 'Account does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)



"""
Create a new budget for a particular user account
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def Budget(request):
    if request.method == "POST":
        account = request.data.get("account", "")
        user = request.user
        amount = request.data.get("amount", "")
        category = request.data.get("category", "")
        name = request.data.get("name","")

        if not amount or not name or not category:
            return JsonResponse({'message': 'Please fill all fields in form','error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            try:
                account = Account.objects.get(id=account)
                budget = Budget.objects.create(user=user,account=account,amount=amount,name=name,category=category)
                budget.save()
                return JsonResponse({'message': 'Budget saved successfully','error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
            except Account.DoesNotExist:
                return JsonResponse({'message': 'Account does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


"""
Edit budget for a particular user account
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def EditBudget(request, budget_id):
    if request.method == "POST":
        account = request.data.get("account", "")
        user = request.user
        amount = request.data.get("amount", "")
        category = request.data.get("category", "")
        name = request.data.get("name","")

        if not amount or not name or not category:
            return JsonResponse({'message': 'Please fill all fields in form','error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                budget = Budget.objects.get(id=budget_id)
            except Budget.DoesNotExist:
                return JsonResponse({'message': 'Budget does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

            try:
                account = Account.objects.get(id=account)
                budget.account=account
                budget.amount=amount
                budget.name=name
                budget.category=category
                budget.save(update_fields=["account","amount","name","category"])
                return JsonResponse({'message': 'Budget saved successfully','error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
            except Account.DoesNotExist:
                return JsonResponse({'message': 'Account does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

"""
Delete a budget for a particular user account
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def DeleteBudget(request, budget_id):
    if request.method == "POST":
        try:
            budget = Budget.objects.get(id=budget_id)
            budget.delete()
            return JsonResponse({'message': 'Budget deleted successfully','error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'message': 'Budget does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


"""
List transactions for a particular user account
"""
@api_view(['GET'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def ListTransaction(request, account_id):

    try:
        account = Account.objects.get(id=account_id)
        transaction = Transaction.objects.filter(user=request.user, account=account)

        transaction = TransactionSerializer(transaction,many=True)
        return JsonResponse({'transaction':transaction.data,'error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return JsonResponse({'message': 'Account does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)



"""
Create a new transaction for a particular user account
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def Transactions(request):
    if request.method == "POST":
        account = request.data.get("account")
        user = request.user
        amount = request.data.get("amount")
        payee = request.data.get("payee")
        category = request.data.get("category")
        transaction_type = request.data.get("transaction_type")
        created_at = request.data.get("startDate")
        updated_at = request.data.get("startDate")

        if not amount or not payee or not category:
            return JsonResponse({'message': 'Please fill all fields in form','error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            try:
                account = Account.objects.get(id=account)
                transaction = Transaction.objects.create(user=user,created_at=created_at, updated_at=updated_at,account=account,amount=amount,payee=payee,category=category,transaction_type=transaction_type)
                transaction.save()
                transaction = TransactionSerializer(transaction, many=False)
                return JsonResponse({'message': 'Transaction saved successfully','data':transaction.data ,'error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
            except Account.DoesNotExist:
                return JsonResponse({'message': 'Account does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


"""
Update a transaction for a particular user account
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def UpdateTransaction(request, transaction_id):
    if request.method == "POST":
        account = request.data.get("account", "")
        user = request.user
        amount = request.data.get("amount", "")
        payee = request.data.get("payee", "")
        category = request.data.get("category", "")
        created_at = request.data.get("created_at", "")
        transaction_type = request.data.get("transaction_type","")

        if not amount or not payee or not category:
            return JsonResponse({'message': 'Please fill all fields in form','error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            try:
                transaction = Transaction.objects.get(id=transaction_id)
            except:
                return JsonResponse({'message': 'Transaction does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            try:
                account = Account.objects.get(id=account)
                transaction.account=account
                transaction.amount=amount
                transaction.payee=payee
                transaction.category=category
                transaction.created_at = created_at
                transaction.updated_at = datetime.datetime.now()
                transaction.transaction_type=transaction_type
                transaction.save(update_fields=["account","amount","payee","category","transaction_type"])
                return JsonResponse({'message': 'Transaction updated successfully','error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
            except Account.DoesNotExist:
                return JsonResponse({'message': 'Account does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


"""
Delete a transaction for a particular user account
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def DeleteTransaction(request, transaction_id):
    if request.method == "POST":
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            transaction.delete()
            return JsonResponse({'message': 'Transaction deleted successfully','error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'message': 'Transaction does not exist','error':False,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

"""
Create a new account for a user
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def CreateAccount(request):
    if request.method == "POST":
        user = request.user
        name = request.data.get("name")
        category = request.data.get("category")
        current_balance = request.data.get("amount")

        if not name or not category or not current_balance:
            return JsonResponse({'message': 'Please fill all fields in form','error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            account = Account.objects.create(user=user,name=name,category=category,current_balance=current_balance)
            account.save()
            account = AccountSerializer(account, many=False)
            return JsonResponse({'message': 'Account created successfully','data':account.data,'error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)



"""
Update a user account information
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def EditAccount(request, account_id):
    if request.method == "POST":
        user = request.user
        name = request.data.get("name", "")
        category = request.data.get("category", "")
        updated_at = datetime.datetime.now()
        try:
            account = Account.objects.get(id=account_id)
            account.name = name
            account.category = category
            account.updated_at = updated_at
            account.save(update_fields=["name","category","updated_at"])
            return JsonResponse({'message': 'Account updated successfully','error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except  Account.DoesNotExist:
            return JsonResponse({'message': 'Account does not exist','error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        








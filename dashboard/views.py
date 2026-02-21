from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from transactions.models import Transaction
from django.db.models import Sum


class DashboardSummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        transactions = Transaction.objects.filter(user=user)

        total_income = transactions.filter(type='income').aggregate(
            total=Sum('amount'))['total'] or 0

        total_expenses = transactions.filter(type='expense').aggregate(
            total=Sum('amount'))['total'] or 0

        net_savings = total_income - total_expenses

        savings_percentage = (net_savings / total_income * 100) if total_income > 0 else 0

        # Category breakdown
        expense_transactions = transactions.filter(type='expense')
        category_breakdown = {}
        for t in expense_transactions:
            category_breakdown[t.category] = category_breakdown.get(t.category, 0) + float(t.amount)

        return Response({
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_savings': net_savings,
            'savings_percentage': round(savings_percentage, 2),
            'category_breakdown': category_breakdown,
        })
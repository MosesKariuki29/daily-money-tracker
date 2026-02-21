from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from transactions.models import Transaction
from django.db.models import Sum


class InsightsView(APIView):
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

        # Rule-based insight generation
        if savings_percentage >= 20:
            recommendation_type = 'investment'
            description = 'Great job! You are saving over 20% of your income. Consider investing in bonds or a savings fund to grow your wealth.'
            suggested_amount = round(float(net_savings) * 0.5, 2)
        elif 10 <= savings_percentage < 20:
            recommendation_type = 'saving'
            description = 'You are on the right track. Keep maintaining your savings habit and look for small ways to reduce expenses.'
            suggested_amount = round(float(net_savings) * 0.3, 2)
        else:
            recommendation_type = 'saving'
            description = 'Your savings are below 10%. Try to reduce non-essential expenses like dining out or subscriptions.'
            suggested_amount = None

        return Response({
            'recommendation_type': recommendation_type,
            'description': description,
            'suggested_amount': suggested_amount,
            'savings_percentage': round(savings_percentage, 2),
        })
import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class SomeUserCreate(APIView):
    """
    Example JSON-request:
    {
        "id": 1,
        "first_name": "Radif",
        "second_name": "Kurbanov",
        "email": "lol@kek.ru"
    }

    Response the 201 HTTP-status and created data if all ok or detail errors and 400 HTTP-status.
    """
    @staticmethod
    def post(request, *args, **kwargs):
        new_user = UserSerializer(data=request.data)

        if new_user.is_valid():
            new_user.save()
            return Response(new_user.data, status=status.HTTP_201_CREATED)

        return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)


class SomeUserView(APIView):
    """
    Show the information about user.
    """
    @staticmethod
    def get(request, user_id, *args, **kwargs):
        user = SomeUser.objects.filter(id=user_id)

        if len(user) == 0:
            return Response({"Bad Request": "No user with such id"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user[0])

        return Response(serializer.data, status=status.HTTP_200_OK)


class SomeUserChange(APIView):
    """
    Change the information about user.

    {
        "email": "mem@ya.ru"
    }


    Response the 200 HTTP-status and changed data if all ok or detail errors and 400 HTTP-status.

    """
    @staticmethod
    def patch(request, user_id, *args, **kwargs):
        user = SomeUser.objects.filter(id=user_id)

        if len(user) == 0:
            return Response({"Bad Request": "No user with such id"}, status=status.HTTP_400_BAD_REQUEST)

        user = user[0]

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SomeUserDelete(APIView):
    """
    Delete the user by id.
    """
    @staticmethod
    def delete(request, user_id, *args, **kwargs):
        snippet = SomeUser.objects.filter(id=user_id)
        if len(snippet) == 0:
            return Response({"Bad Request": "No user with such id"}, status=status.HTTP_400_BAD_REQUEST)

        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IncomeCreate(APIView):
    """
    Create the new income.

    Example JSON-request data:
    {
        "id": 1,
        "user_id": 1,
        "amount": 19.13,
        "date": "2021-05-26"
    }

    Response the 201 HTTP-status and created data if all ok or detail errors and 400 HTTP-status.
    """
    @staticmethod
    def post(request, *args, **kwargs):
        new_income = IncomeSerializer(data=request.data)

        if request.data['date'] > datetime.date:
            return Response({"Bad Request": "Wrong date"}, status=status.HTTP_400_BAD_REQUEST)

        if new_income.is_valid():
            new_income.save()
            return Response(new_income.data, status=status.HTTP_201_CREATED)

        return Response(new_income.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeView(APIView):
    """
    Show the information about income by id.
    """
    @staticmethod
    def get(request, income_id, *args, **kwargs):
        income = Income.objects.filter(id=income_id)

        if len(income) == 0:
            return Response({"Bad Request": "No income with such id"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = IncomeSerializer(income[0])

        return Response(serializer.data, status=status.HTTP_200_OK)


class IncomeChange(APIView):
    """
    Change the income information.

    Example JSON-request data:
    {
        "amount": 10.21,
        "date": "2021-05-20"
    }

    Response the 200 HTTP-status if all ok or detail errors and 400 HTTP-status.
    """
    @staticmethod
    def patch(request, income_id, *args, **kwargs):
        income = Income.objects.filter(id=income_id)

        if len(income) == 0:
            return Response({"Bad Request": "No income with such id"}, status=status.HTTP_400_BAD_REQUEST)

        if 'date' in request.data:
            if request.data['date'] > datetime.date:
                return Response({"Bad Request": "Wrong date"}, status=status.HTTP_400_BAD_REQUEST)

        income = income[0]

        serializer = IncomeSerializer(income, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeDelete(APIView):
    """
    Delete the income by id.
    """
    @staticmethod
    def delete(request, income_id, *args, **kwargs):
        snippet = Income.objects.filter(id=income_id)
        if len(snippet) == 0:
            return Response({"Bad Request": "No income with such id"}, status=status.HTTP_400_BAD_REQUEST)

        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IncomesSum(APIView):
    """
    Calculate the sum of incomes.
    Hash table store a dates and sum: {date: sum}
    Also check the existing user.0
    """
    @staticmethod
    def get(request, user_id, *args, **kwargs):
        incomes = Income.objects.all()
        user = SomeUser.objects.filter(id=user_id)

        if len(user) == 0:
            return Response({"Bad Request": "No user with such id"}, status=status.HTTP_400_BAD_REQUEST)

        hash_table = dict()

        for income in incomes:
            if income.user_id == user_id:
                if income.date not in hash_table:
                    hash_table[income.date] = income.amount
                else:
                    hash_table[income.date] += income.amount

        lst_sums = [{"date": key, "sum": hash_table[key]} for key in hash_table]

        return Response({"Summary": lst_sums})


class OutcomeCreate(APIView):
    """
    Create the new outcome.

    Example JSON-request data:
    {
        "id": 1,
        "user_id": 1,
        "amount": 12.21,
        "date": "2021-05-26"
    }

    Response the 201 HTTP-status if all ok or detail errors and 400 HTTP-status.
    """
    @staticmethod
    def post(request, *args, **kwargs):
        new_outcome = OutcomeSerializer(data=request.data)

        if request.data['date'] > datetime.date:
            return Response({"Bad Request": "Wrong date"}, status=status.HTTP_400_BAD_REQUEST)

        if new_outcome.is_valid():
            new_outcome.save()
            return Response(new_outcome.data, status=status.HTTP_201_CREATED)

        return Response(new_outcome.errors, status=status.HTTP_400_BAD_REQUEST)


class OutcomeView(APIView):
    """
    Show the outcome information.
    """
    @staticmethod
    def get(request, outcome_id, *args, **kwargs):
        outcome = Outcome.objects.filter(id=outcome_id)

        if len(outcome) == 0:
            return Response({"Bad Request": "No outcome with such id"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = IncomeSerializer(outcome[0])

        return Response(serializer.data, status=status.HTTP_200_OK)


class OutcomeChange(APIView):
    """
    Change the outcome information.

    Example JSON-request data:
    {
        "amount": 10.21,
        "date": "2021-05-20"
    }

    Response the 200 HTTP-status if all ok or detail errors and 400 HTTP-status.

    """
    @staticmethod
    def patch(request, outcome_id, *args, **kwargs):
        outcome = Outcome.objects.filter(id=outcome_id)

        if len(outcome) == 0:
            return Response({"Bad Request": "No outcome with such id"}, status=status.HTTP_400_BAD_REQUEST)

        outcome = outcome[0]

        if 'date' in request.data:
            if request.data['date'] > datetime.date:
                return Response({"Bad Request": "Wrong date"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = OutcomeSerializer(outcome, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OutcomeDelete(APIView):
    """
    Delete the outcome by id.
    """
    @staticmethod
    def delete(request, outcome_id, *args, **kwargs):
        snippet = Outcome.objects.filter(id=outcome_id)
        if len(snippet) == 0:
            return Response({"Bad Request": "No outcome with such id"}, status=status.HTTP_400_BAD_REQUEST)

        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OutcomesSum(APIView):
    """
    Calculate the sum of outcomes.
    Hash table store a dates and sum: {date: sum}
    Also check the existing user.
    """
    @staticmethod
    def get(request, user_id, *args, **kwargs):
        outcomes = Outcome.objects.all()
        user = SomeUser.objects.filter(id=user_id)

        if len(user) == 0:
            return Response({"Bad Request": "No user with such id"}, status=status.HTTP_400_BAD_REQUEST)

        hash_table = dict()

        for outcome in outcomes:
            if outcome.user_id == user_id:
                if outcome.date not in hash_table:
                    hash_table[outcome.date] = outcome.amount
                else:
                    hash_table[outcome.date] += outcome.amount

        lst_sums = [{"date": key, "sum": hash_table[key]} for key in hash_table]

        return Response({"Summary": lst_sums}, status=status.HTTP_200_OK)

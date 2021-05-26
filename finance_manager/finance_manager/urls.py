from django.contrib import admin
from django.urls import path
from src.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', SomeUserCreate.as_view()),  # create a user. POST: user/
    path('user/<int:user_id>', SomeUserView.as_view()),  # show the info about user. GET: user/1
    path('change_user/<int:user_id>', SomeUserChange.as_view()),  # change the information about user. PATCH: user/1
    path('del_user/<int:user_id>', SomeUserDelete.as_view()),  # delete the user by id. DELETE: user/1
    path('income/', IncomeCreate.as_view()),  # create a new income. POST: income/
    path('income/<int:income_id>', IncomeView.as_view()),  # show the info about income. GET: income/2
    path('change_income/<int:income_id>', IncomeChange.as_view()),  # change the info about income. PATCH: income/2
    path('del_income/<int:income_id>', IncomeDelete.as_view()),  # delete the income by id. DELETE: income/2
    path('sum_incomes/<int:user_id>', IncomesSum.as_view()),  # calculate the sum BY USER ID. GET: income/1
    path('outcome/', OutcomeCreate.as_view()),  # create the new outcome. POST: outcome/
    path('outcome/<int:outcome_id>', OutcomeView.as_view()),  # show the info about outcome. GET: outcome/3
    path('change_outcome/<int:outcome_id>', OutcomeChange.as_view()),  # change the info about outcome. PATCH: outcome/3
    path('del_outcome/<int:outcome_id>', OutcomeDelete.as_view()),  # delete the outcome by id. DELETE: outcome/3
    path('sum_outcomes/<int:user_id>', OutcomesSum.as_view())  # calculate the sum of user outcomes. GET: outcome/1
]

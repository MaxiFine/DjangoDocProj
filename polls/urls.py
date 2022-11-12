from django.urls import path
from .views import detail, results, vote, index

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/', results, name='results'),
    path('<int:question_id>/', vote, name='vote'),

]

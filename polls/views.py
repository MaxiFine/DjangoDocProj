from django.shortcuts import render, HttpResponse
from .models import Question

# Create your views here.
def index(request):
    question = Question.objects.order_by('-pub_date'[:5])
    output = ', '.join([q.question_text for q in question]) # list comprehension here
    return HttpResponse(output)

    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of the question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


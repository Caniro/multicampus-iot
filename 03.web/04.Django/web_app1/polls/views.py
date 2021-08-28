from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.all()\
            .order_by('-pub_date')[:5] # -는 내림차순
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # # .get 메서드는 결과가 한 행이 아니면 예외 발생
    # context = {'question': Question.objects.get(id=question_id)}
    # return render(request, 'polls/detail.html', context)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', { "question": question })

def vote(request, question_id):
    # print('-'*80)
    # print("Header", request.headers, sep='\n')
    # print("\nGET", request.GET, sep='\n')
    # print("\nPOST", request.POST, sep='\n')
    # print("\nBody", request.body, sep='\n')
    # print('-'*80)
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        choice = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice)
    except:
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return render(request, 'polls/results.html', {'question': question}) # 새로고침할 때마다 투표됨
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

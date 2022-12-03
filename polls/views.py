from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Question , Choice 
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def IndexView(request):
	question_list = Question.objects.order_by('-date_posted')
	return render(request,'polls/f1.html',{'question_list':question_list})


@login_required
def results(request , question_id):
	question = get_object_or_404(Question ,pk = question_id)
	return render(request , 'polls/results.html' , {'question':question})


@login_required
def vote(request , question_id):
	question = get_object_or_404(Question , pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except(KeyError , Choice.DoesNotExist):
		return render(request,'polls/error.html' , {'question' : question,'error_message' : "You didn't select a choice"})
	else :
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('results', args =(question.id, )))

	
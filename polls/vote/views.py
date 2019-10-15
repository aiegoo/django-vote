
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

# Create your views here.

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'vote/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
			pub_date_lte=timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'vote/detail.html'
	def get_queryset(self):
		"""
		exclude any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'vote/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (keyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'vote/detail.html', {
			'question': question,
			'error_message': "you didn't select a choice.",
		})
	else:
		selected_choice_votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('vote:results', args=(question.id,)))

# def detail(request, question_id):
	# question = get_object_or_404(Question, pk=question_id)
	# return render(request, 'vote/detail.html', {'question': question})

""" def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'vote/results.html', {'question': question}) """

def vote(request, question_id):
	return HttpResponse("you are voting on question %s." % question_id)

from .models import Question

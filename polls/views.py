from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    # when we want to override ListView's automatically
    # generated context variable `question_list`, we can
    # employ the `context_object_name` attribute to
    # specify a context variable of our own
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Mate! You didn't select a choice!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # always return an HttpResponseRedirect following a
        # successful POST transaction; this prevents data from
        # being posted twice if the user hits the Back button
        return HttpResponseRedirect(reverse('polls:results',
args=(question.id,)))
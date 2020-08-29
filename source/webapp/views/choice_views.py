from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from webapp.models import Choice, Poll
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoiceForm, SearchForm
from django.db.models import Q


class ChoiceCreateView(CreateView):
    template_name = 'choices/choice_create.html'
    form_class = ChoiceForm
    model = Choice

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)


# class TaskUpdateView(UpdateView):
#     template_name = 'task/task_update.html'
#     form_class = TaskForm
#     model = Tasks
#     context_object_name = 'task'
#
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.object.pk})
#
#
# class TaskDeleteView(DeleteView):
#     template_name = 'task/task_delete.html'
#     model = Tasks
#     success_url = reverse_lazy('index')
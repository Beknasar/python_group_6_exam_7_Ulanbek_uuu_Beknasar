from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import View

from webapp.models import Poll, Choice
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm, PollForm
from django.db.models import Q

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        kwargs['form'] = form
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Poll.objects.all()

        form = SearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(question__icontains=search))

        return data.order_by('-date_create')

class PollView(DetailView):
    template_name = 'polls/poll_view.html'
    model = Poll
    paginate_choice_by = 5
    paginate_choice_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        choices, page, is_paginated = self.paginate_tasks(self.object)
        context['choices'] = choices
        context['page_obj'] = page
        context['is_paginated'] = is_paginated

        return context

    def paginate_tasks(self, poll):
        choices = poll.choices.all()
        if choices.count() > 0:
            paginator = Paginator(choices, self.paginate_choice_by, orphans=self.paginate_choice_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1  # page.has_other_pages()
            return page.object_list, page, is_paginated
        else:
            return choices, None, False


class PollCreateView(CreateView):
    template_name = 'polls/poll_create.html'
    form_class = PollForm
    model = Poll
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'polls/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('index')


class PollUpdateView(UpdateView):
    template_name = 'polls/poll_update.html'
    form_class = PollForm
    model = Poll
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class AnswerView(View):
    data = {}
    for choice in Choice.objects.all():
        data.update({f'{choice.text}': int(0)})

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=pk)
        return render(request, 'answer.html', context={'poll': poll, 'data': self.data})

    def post(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        try:
            selected_choice = poll.choices.get(pk=request.POST.get('choice'))
            print(selected_choice.text)
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'answer.html', {
                'poll': poll,
                'error_message': "You didn't select a choice.",
            })
        else:
            for key, value in self.data.items():
                if key == selected_choice.text:
                    value +=1
                self.data.update({key:value})
            print(self.data)

        # for key, value in self.data:
        #     print(f'{key}  Количество: {value}')
        return redirect('index')
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy

from webapp.models import Poll
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

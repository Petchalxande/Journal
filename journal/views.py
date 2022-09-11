from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404, render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

from .models import Entry
from .forms import EntryCreateForm, EntryUpdateForm
from .utils import searchEntries


def entryListView(request):
    
    user_entries = Entry.objects.filter(author=request.user)

    paginator = Paginator(user_entries, 6)
    page = request.GET.get('page')
    user_entries = paginator.get_page(page)

    context = {
        'journal_entries': user_entries,
    }

    return render(request, 'journal/entry-list.html', context)



@login_required
def entryDetailView(request, pk):
    entry = get_object_or_404(Entry, pk=pk)

    if entry.author == request.user:

        context = {
            'entry': entry,
        }
        return render(request, 'journal/entry-detail.html', context)

    else:
        raise PermissionDenied()


def toggleBookmarkView(request, pk):

    if request.method == 'POST':

        entry = Entry.objects.get(id=pk)
        if entry.bookmarked:
            entry.bookmarked = False
        else:
            entry.bookmarked = True
        entry.save()

        return HttpResponseRedirect(reverse_lazy('entry_detail', args=[entry.id]))

    else:
        return HttpResponseRedirect(reverse_lazy('entry_detail', args=[entry.id]))



class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryCreateForm
    template_name = 'journal/entry-create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    form_class = EntryUpdateForm
    template_name = 'journal/entry-update.html'


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'journal/entry-delete.html'
    success_url = reverse_lazy('entry_list')


class BookmarkedEntriesListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'journal/bookmarked-entries-list.html'
    context_object_name = 'bookmarked_entries'
    paginate_by = 6

    def get_context_data(self):
        user_entries = Entry.objects.filter(author=self.request.user)
        bookmarked_entries = user_entries.filter(bookmarked=True)

        context = {
            'bookmarked_entries': bookmarked_entries,
        }

        return context


class SearchEntriesView(LoginRequiredMixin, TemplateView):
    template_name = 'journal/search-entries.html'


@login_required
def searchEntriesListView(request):

    if request.GET:
        search_results, search_query = searchEntries(request)

        context = {
            'search_query': search_query,
            'journal_entries_search_results': search_results
        }

        return render(request, 'journal/search-entries-results.html', context)

    return render(request, 'journal/search-entries-results.html')

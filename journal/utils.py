from .models import Entry
from django.db.models import Q


def searchEntries(request):

    search_query = request.GET.get('q')

    if not search_query:
        searchResults = Entry.objects.none()

    else:
        searchResults = Entry.objects.none()

        for queried_term in search_query.split(','):

            queried_term = queried_term.strip()
            searchResults = searchResults | Entry.objects.filter(
                Q(title__icontains=queried_term) |
                Q(quotee__icontains=queried_term) |
                Q(quotation__icontains=queried_term)
                ).distinct()

    return searchResults[0:50], search_query
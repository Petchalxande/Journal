from .models import Entry
from django.db.models import Q


def searchEntries(request):

    search_query = ''

    if request.GET.get('q'):
        search_query = request.GET.get('q')

    # First filter for all of users journal entries
    user_entries = Entry.objects.filter(author=request.user)

    # Filter the users entries by search term
    searchresults = user_entries.filter(
        Q(title__icontains=search_query)|
        Q(body__icontains=search_query)
    ).order_by('-created')

    return searchresults, search_query

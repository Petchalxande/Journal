from django.urls import path
from .views import (
    entryListView,
    entryDetailView,
    toggleBookmarkView,
    EntryCreateView,
    EntryUpdateView,
    EntryDeleteView,
    BookmarkedEntriesListView,
    SearchEntriesView,
    searchEntriesListView
)


urlpatterns = [
    path('', entryListView, name='entry_list'),
    path('entry/<str:pk>/', entryDetailView, name='entry_detail'),
    path('toggle-bookmark/<str:pk>/', toggleBookmarkView, name='toggle_bookmark'),
    path('create/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/update/<str:pk>/', EntryUpdateView.as_view(), name='entry_update'),
    path('entry/delete/<str:pk>/', EntryDeleteView.as_view(), name='entry_delete'),
    path('bookmarked-entries/', BookmarkedEntriesListView.as_view(), name='bookmarked_entries'),
    path('search/', SearchEntriesView.as_view(), name='search-entries'),
    path('search-results/', searchEntriesListView, name='search-entries-results'),
]

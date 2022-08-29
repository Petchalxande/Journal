from django.test import TestCase
from .models import Entry

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from django.urls import reverse


class NewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'TestUser',
            email = 'testuser@email.com',
            password = 'testpass123'
        )

        # Get permissions and assign to class variables
        self.view_news = Permission.objects.get(codename='view_entry')
        self.update_news = Permission.objects.get(codename='change_entry')
        self.delete_news = Permission.objects.get(codename='delete_entry')

        # Create the test post
        self.entry = Entry.objects.create(
            title= "Test Entry Title",
            author = get_user_model().objects.get(email="testuser@email.com"),
            body = "This is some content"
            )

        self.entry_id = self.entry.id


    #Tests the string return method
    def test_string_representation(self):
        self.assertEqual(str(self.entry), "Test Entry Title")


    # Tests entry was created correctly
    def test_post_content(self):
        self.assertIsNotNone(self.entry.id)
        self.assertEqual(self.entry.author.email, "testuser@email.com")
        self.assertEqual(self.entry.title, "Test Entry Title")
        self.assertEqual(self.entry.body, "This is some content")
        self.assertEqual(self.entry.bookmarked, False)

    # Entry List

    # Test if user cannot view entry list when signed out
    def test_redirect_signed_out(self):
        self.client.logout()
        response = self.client.get(reverse('entry_list'))

        # Check for redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/' % (reverse('account_login')))

        # Update response variable following redirect 
        response = self.client.get(
            '%s?next=/' % (reverse('account_login')))

        # Check redirected to login page
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'login')


    # Test if user can view entry list when signed in
    def test_view_listpage_logged_in(self):
        self.client.login(email="testuser@email.com", password="testpass123")
        response = self.client.get(reverse('entry_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journal/entry-list.html')


    # Detail View

    # Tests if users can view news posts when logged in
    def test_view_detail_logged_in(self):
        self.client.login(email="testuser@email.com", password="testpass123")
        response = self.client.get(self.entry.get_absolute_url())

        # Check page loads / template / content
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journal/entry-detail.html')
        self.assertContains(response, 'Test Entry Title')

        # Check bad url returns 404
        no_response = self.client.get(f'/entry/AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA/')
        self.assertEqual(no_response.status_code, 404)


    # Tests if users can view entry update / delete page when logged
    def test_view_update_delete_logged_in(self):
        self.client.login(email="testuser@email.com", password="testpass123")

        response = self.client.get(f'/entry/update/{self.entry_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journal/entry-update.html')

        response = self.client.get(f'/entry/delete/{self.entry_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journal/entry-delete.html')
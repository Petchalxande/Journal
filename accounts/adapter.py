from allauth.account.adapter import DefaultAccountAdapter

from config.settings import OPEN_FOR_SIGNUP


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):

        if OPEN_FOR_SIGNUP:
            return True
        else:
            return False

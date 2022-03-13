from django.test import TestCase


"""
To make a test API call over an authenticated API endpoint, follow
this pattern:


```
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()
user = ...
client.force_authenticate(user=self.user)
response = client.get(reverse('{REVERSED_URL}'))
```

"""

from django.test import TestCase

from directory.models import User, Company


class UserTestCase(TestCase):
    def test_user(self):
        
        User.objects.create(
            username='user', first_name='zayneb', last_name='hammami', company=Company.objects.create(name="Company3")
        )
      



class UsersViewSetAPICase(TestCase):

    def setUp(self):
        # TODO
        pass

    def test_something(self):
        # TODO
        pass



### Requirements
- Docker

### Set-up Instructions
This project is already fully configured to launch. You will only need to add data to the DB to get started.

Clone this repository, navigate into the root directory, and boot up using `docker-compose up directory`. This command will pull the base python image, install requirements, migrate and launch the local server.

To add some data, open another shell and connect to the running container with `docker-compose exec directory bash`. You can then navigate into the directory `cd mysite`, and launch the shell with `./manage.py shell`.

### Data & Models
The models in this app are very simple. There are only 3 you need to worry about:
1) The `User` model. This model contains basic attributes from Django, with only the addition of `Company` and `reports_to` foreign keys.
2) The `Company` model. All `User`s have a `Company`. It is a natural grouping for a Enterprise SaaS product.
3) The `Token` object (`from rest_framework.authtoken.models import Token`). This will be used for authenticating a `User` over the API.

To add some data, you can use `create_user`.
```python
>>> from directory.models import *
>>> company = Company.objects.create(name="Test Company")  # Create a new Company
>>> user = User.objects.create_user(username=..., first_name=..., last_name=..., company=company)  # Add a user to the Company.
>>> from rest_framework.authtoken.models import Token  # Import the Token model
>>> token = Token.objects.create(user=user)  # Create an API Token for this new user.
>>> print(token.key)  # Display the API key for this User.
```




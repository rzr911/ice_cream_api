# Setup
1. Clone the repo and build `docker-compose -f local.yml build`
2. Run migrations `docker-compose -f local.yml run django python manage.py migrate`
3. Create a user `docker-compose -f local.yml run django python manage.py createsuperuser`

# API Doc
[Postman Link](https://www.getpostman.com/collections/faa2609057132574f0fb)

# Notes
1. You'd need docker and docker-compose installed to run this project.
2. All APIs except `/api/token` require JWT token. Add the access token received from the token API as a `Authorization` header in the following format: `Bearer {access_token}`

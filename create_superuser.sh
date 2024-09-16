#!/bin/bash

# Define the environment variables or hardcode the superuser credentials
SUPERUSER_EMAIL="mujtabajafri3@gmail.com"
SUPERUSER_PASSWORD="pass"
SUPERUSER_NAME="pass"
# Create superuser non-interactively
python bhr/manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput

# Use Django shell to set the password for the superuser
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
user = User.objects.get(email='$SUPERUSER_EMAIL'); \
user.set_password('$SUPERUSER_PASSWORD'); \
user.save()" | python bhr/manage.py shell

echo "Superuser created with email: $SUPERUSER_EMAIL"
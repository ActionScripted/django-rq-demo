FROM python:3

# We want proper container logging
ENV PYTHONUNBUFFERED 1

# Move requirements file into container
ADD requirements.txt /django-rq/requirements.txt

# Set working directory to project
WORKDIR /django-rq/

# Upgrade pip
RUN pip install --upgrade pip
# Install requirements
RUN pip install -r requirements.txt

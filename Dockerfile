FROM python:3.8.10

RUN apt-get update && apt-get install build-essential -y

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /Personalised_multi_User_system
WORKDIR /Personalised_multi_User_system

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /Personalised_multi_User_system/
RUN pipenv install --system


COPY . /Personalised_multi_User_system/

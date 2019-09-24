FROM python:3-alpine
WORKDIR 
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install -r requirements.txt
ENV DEVELOPER="Boris Rendon"
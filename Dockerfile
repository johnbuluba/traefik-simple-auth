FROM python:3.7-alpine3.8

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

RUN mkdir /traefikauth &&\
    pip3 install pipenv

ADD Pipfile* /traefikauth/


RUN cd /traefikauth &&\
    pipenv install --system

ADD deploy /traefikauth/deploy

ADD traefikauth /traefikauth/traefikauth

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE traefikauth.settings.docker
CMD ["/traefikauth/deploy/start.sh"]
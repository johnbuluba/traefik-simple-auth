FROM python:3.7-alpine3.8

RUN mkdir /traefikauth &&\
    pip3 install pipenv

ADD Pipfile* /traefikauth/


RUN cd /traefikauth &&\
    pipenv install --system

ADD deploy /traefikauth/deploy

ADD traefikauth /traefikauth/traefikauth

EXPOSE 8000

CMD ["/traefikauth/deploy/start.sh"]
FROM python:3

MAINTAINER Lucas Vieira Felipe

ADD . /testemax

WORKDIR /testemax

#RUN apt-get update -y
#RUN apt-get install -y python-pip
RUN pip install -r requirements.txt && pip freeze > requirements.txt
RUN chmod 644 app.py
CMD ["python", "app.py"]

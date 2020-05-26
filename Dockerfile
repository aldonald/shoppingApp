FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /shopping
WORKDIR /shopping
ADD . /shopping/
RUN pip install -r requirements.txt

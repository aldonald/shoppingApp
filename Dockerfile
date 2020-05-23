FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /shoppinglist
WORKDIR /shoppinglist
ADD . /shoppinglist/
RUN pip install -r requirements.txt

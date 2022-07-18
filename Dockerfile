# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /product_service
COPY requirements.txt /product_service/
RUN pip install -r requirements.txt
COPY . /product_service/

CMD python /product_service/manage.py migrate && python /product_service/manage.py runserver 0.0.0.0:8000
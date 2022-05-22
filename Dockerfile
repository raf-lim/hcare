FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
COPY requirements/base.txt /code/
COPY requirements/local.txt /code/
RUN pip install -r local.txt
RUN apt update
RUN apt install gettext -y
COPY . /code/

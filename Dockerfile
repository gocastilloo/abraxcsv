FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin libgdal-dev
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -U pip setuptools
RUN pip install -r requirements.txt
COPY . /code/


FROM python:latest
MAINTAINER Kourosh Parsa

RUN apt-get update -y
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y net-tools
RUN apt-get install -y python3-pip
RUN apt-get install -yq tzdata
RUN ln -fs /usr/share/zoneinfo/America/Vancouver /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt-get install -y procps
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
COPY app /app/app
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8081", "--reload"]

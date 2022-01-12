FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev build-essential

WORKDIR /scooter

COPY requirements.txt requirements.txt

RUN pip3 install -r ./requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]

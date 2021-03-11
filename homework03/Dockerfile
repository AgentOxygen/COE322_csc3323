FROM ubuntu:latest

RUN apt-get update -y --fix-missing
RUN apt-get install -y python python-pip python-dev build-essential

COPY . /app
WORKDIR /app

ENV LC_CTYPE=en_US.UTF-8
ENV LANG=en_US.UTF-8

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
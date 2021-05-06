FROM ubuntu

ADD . ./app

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip install -r /app/requirements.txt
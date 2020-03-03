FROM debian:stable-slim
RUN apt-get update
RUN apt-get -y install python3
RUN apt install -y python3-pip

COPY . /app
WORKDIR /app/src
RUN pip3 install -r ../requirements.txt
ENV FLASK_APP api.py
EXPOSE 5005
CMD flask run --host=0.0.0.0 --port=5005
#CMD python3 api.py

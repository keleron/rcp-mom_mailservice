FROM ubuntu
RUN apt-get update -y; \
	apt-get install python3 -y;  \
	apt-get install rabbitmq-server -y;  \
	apt-get install python3-pip -y; \
	pip3 install pika
COPY /Sender.py /SD/Sender.py
VOLUME /app
WORKDIR SD
CMD python3 Sender.py
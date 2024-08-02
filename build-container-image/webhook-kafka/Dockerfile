# Inherit python image
FROM python:3.6-slim

#add the variables used to build the Python app

ARG BOOTSTRAP_SERVER="172.30.113.193:9092"
ARG KAFKA_TOPIC="acs-topic"
ARG WEBHOOK_ROUTE="/webhook"

ENV BOOTSTRAP_SERVER=$BOOTSTRAP_SERVER
ENV KAFKA_TOPIC=$KAFKA_TOPIC
ENV WEBHOOK_ROUTE=$WEBHOOK_ROUTE

# Set up directories
RUN mkdir /application
WORKDIR /application

# Copy python dependencies and install these
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the rest of the applicationssd
COPY . .

# Environment variables
ENV PYTHONUNBUFFERED 1

# EXPOSE port 8001 to allow communication to/from server
EXPOSE 8001
STOPSIGNAL SIGINT

ENTRYPOINT ["python"]
CMD ["webhook-kafka.py"]

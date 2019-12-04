FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3

COPY pi.py /code/pi.py

RUN chmod +x /code/pi.py

ENV PATH "/code:$PATH"

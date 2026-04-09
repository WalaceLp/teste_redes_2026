FROM ubuntu:26.04
RUN apt update -y
RUN apt install iproute2 -y
RUN apt install python3 -y
CMD ["python3", "/app/server.py" ]
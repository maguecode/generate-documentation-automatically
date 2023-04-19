FROM ubuntu:22.10

RUN apt-get -qq update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y build-essential cmake
RUN pip install sphinx

WORKDIR /home/generate-documentation-automatically
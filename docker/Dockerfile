FROM ubuntu:22.10

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update
RUN apt-get install --no-install-recommends -y sudo
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y build-essential cmake git wget
RUN pip install sphinx

WORKDIR /home/generate-documentation-automatically
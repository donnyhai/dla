FROM nvidia/cuda:10.2-base

RUN apt update && \
	apt install openjdk-8-jdk bash -y && \
	apt install python3-pip bash -y 
	
RUN apt install curl bash -y && \
	apt install git bash -y

RUN apt install vim -y

ENV PATH="/usr/local/lib/python3.6/dist-packages:${PATH}"
ENV PYTHONPATH="/usr/local/lib/python3.6/dist-packages:${PYTHONPATH}"

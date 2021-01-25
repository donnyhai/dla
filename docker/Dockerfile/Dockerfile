FROM nvidia/cuda:10.2-base
#dla:v1

RUN apt update && \
	apt install openjdk-8-jdk bash -y && \
	apt install python3-pip bash -y 
	
RUN apt install python -y
	
RUN apt install curl bash -y && \
	apt install git bash -y

RUN apt install vim -y

RUN pip3 install virtualenv

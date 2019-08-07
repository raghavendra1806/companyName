FROM ubuntu:latest
LABEL maintainer="Raghavendra"
RUN apt-get update
RUN apt-get install python-pip python3 -y
RUN pip install requests
ADD ./companyName.py /root
USER root
WORKDIR /root
CMD ["/bin/bash"]

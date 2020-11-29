FROM ubuntu:18.04

RUN apt update && apt install -y cmake make wget sudo vim

RUN apt update && apt install -y g++-6 g++-7 g++-8 g++-9
RUN apt update && apt install  -y g++-6-aarch64-linux-gnu g++-7-aarch64-linux-gnu \
g++-8-aarch64-linux-gnu

RUN apt update && apt install -y python python3 python3-pip

RUN useradd -r conan -d /home/conan/ -m -u 1000 -s /bin/bash
RUN echo 'conan ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER conan

RUN sudo pip3 install glob2 conan==1.31.0

WORKDIR /home/conan

ADD opencv/ /home/conan/scripts/opencv
ADD conan-config /home/conan/conan-config
RUN conan config install /home/conan/conan-config


#For AI service using cuda
ARG BASE_IMAGE=pytorch/pytorch:2.2.1-cuda11.8-cudnn8-runtime

# #For normal service without using cuda 
# ARG BASE_IMAGE=python:3.10.14-slim-bullseye

FROM ${BASE_IMAGE}

RUN useradd -ms /bin/bash celery_user

COPY requirements.txt /tmp/requirements.txt

WORKDIR /asr

ENV CUDA_DOCKER_ARCH=all

RUN mkdir -p /asr/logs

WORKDIR /asr/src

COPY ./src /asr/src

# RUN modprobe snd-aloop
RUN apt-get update && apt-get install -y build-essential portaudio19-dev pulseaudio
RUN pip install pyaudio ffmpeg
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN chown -R celery_user:celery_user /asr

USER celery_user





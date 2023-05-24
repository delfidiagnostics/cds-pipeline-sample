FROM python:3.9-slim

WORKDIR /dagster/

ENV BUILD_VERSION=dev

COPY requirements.txt ./
COPY surf_l201 ./surf_l201/
COPY cds_pipeline_sample ./cds_pipeline_sample/

RUN pip install -r requirements.txt

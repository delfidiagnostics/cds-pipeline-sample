FROM python:3.9-slim

WORKDIR /dagster/

ENV PYTHONPATH="${PYTHONPATH}:/dagster/"
ENV BUILD_VERSION=dev

RUN mkdir /root/.pip && touch /root/.pip/pip.conf
RUN echo "[global]\nindex-url = https://dsreader:${ARTIFACTORY_PASS}@delfi-artifactory.dev.delfidx.io/artifactory/api/pypi/ds-pypi/simple" > /root/.pip/pip.conf

COPY requirements.txt ./
COPY surf_l201 ./surf_l201/
COPY cds_pipeline_sample ./cds_pipeline_sample/

RUN pip install -r requirements.txt

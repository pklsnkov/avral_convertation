FROM registry.nextgis.com/toolbox-workers/base:1.0.2-ubuntu2004-gdal

COPY . /opt/avral_convertation
RUN pip3 install --no-cache-dir /opt/avral_convertation

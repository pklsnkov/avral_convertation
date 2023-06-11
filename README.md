# avral_convertation

Build

'''
docker build -t avral_convertation:latest .
docker run --rm -t -i -v C:/Users/AntanWind/avral_convertation:/avral_convertation avral_convertation:latest /bin/bash
'''


Run for debug in container

'''
cd avral_converter
pip3 install --no-cache-dir /opt/avral_convertation
pip install geopandas transliterate openpyxl
avral-exec --debug convert source.xlsx
'''

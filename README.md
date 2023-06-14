# avral_convertation

Build

```
docker build -t avral_convertation:latest .
docker run --rm -t -i -v ${PWD}:/avral_convertation avral_convertation:latest /bin/bash
```


Run for debug in container

```
cd /avral_convertation
pip3 install --no-cache-dir /opt/avral_convertation
avral-exec --debug convert /avral_convertation/examples/source.xlsx
```

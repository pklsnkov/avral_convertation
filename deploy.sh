
#send module to toolbox.nextgis.com
docker build --no-cache -t avral_convertation:latest  .
docker tag avral_convertation:latest registry.nextgis.com/toolbox-workers/convertation:prod
docker image push registry.nextgis.com/toolbox-workers/convertation:prod

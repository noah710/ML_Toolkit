#!/bin/bash 
docker build -f Dockerfile -t rstudio-service .  
docker run -it --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" rstudio-service bash

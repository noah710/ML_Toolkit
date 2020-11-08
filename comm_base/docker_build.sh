#!/bin/bash

docker build -f Dockerfile -t comm_base .
docker run -it -p 8888:8888 comm_base bash

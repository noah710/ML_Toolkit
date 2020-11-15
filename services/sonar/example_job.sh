#!/bin/bash

sonar-scanner -Dsonar.projectBaseDir=/usr/src/DVWA

printf "\n\nPlease open a browser to http://localhost:9000 to see results\n"

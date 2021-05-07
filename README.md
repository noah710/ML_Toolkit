# ML_Toolkit

Final project for CS1660 Intro to Cloud Computing
![alt text](https://github.com/noah710/ML_Toolkit/blob/master/demo.png?raw=true)
<br>Demo: https://pitt-my.sharepoint.com/:v:/g/personal/ngl8_pitt_edu/EXLmBRotcDREpNDAA3XJ1PgBOeCo53Y7QkQIv6sXBGHbmA?e=aqtqa0

## System considerations

This has been tested on Ubuntu 20.04. There is no dedicated GPU or CUDA support at this moment, X forwarding has only been verified working on intel integrated graphics.

**Dependencies**
- Docker
- Docker-compose
- golang-docker-credential-helpers (apt package)
## Usage
A fresh build takes about 20 minutes. You can either build the images yourself or pull them from my dockerhub.

Please note that the SHARED folder is mounted in each container!

**Setup instructions**
1. First things first, enable x forwarding with the following command:
```bash
xhost +local:root
```
2. Add a shared directory, and optionally, add any files or repos you'd like in the containers to SHARED
```bash
cd ML_Toolkit
mkdir SHARED
```
3. Either build the images yourself, or pull them from my dockerhub.

**Build yourself** 

```bash
docker-compose build
docker-compose up
```

**Use Dockerhub**
```bash
docker-compose -f dockerhub.yml up
```
4. Open any web browser to `http://localhost/main.html`
5. For subsequent runs, be sure to run `docker-compose down` before running `docker-compose up`

### Regards
- Tableau, Sonarscanner, Hadoop, and Spark may take an extra minute to start up
- Tableau needs a license to activate it
- Tableau login - username: tableau | password: tableau
- Dockerhub - https://hub.docker.com/repository/docker/noah710/ml_toolkit
## Implementation details
**comm_base** - This dir holds a listener which each services uses to listen for triggers to open the application. 
<br/>**server** - Contains a Node webserver that listens for POST requests (button presses) and connects to the relevant service to trigger an application open.
<br/>**services** - Contains dirs for each service, containing at minimum a Dockerfile and open.sh script.
<br/>compose-common.yml - Contains default configuration for a GUI container
<br/><br/>When each service spins up, it runs the comm_base listener which listens for triggers from the web server.
<br/>When the listener hears a trigger, it calls a subprocess to run the open.sh script, which is manually configured for each service. 


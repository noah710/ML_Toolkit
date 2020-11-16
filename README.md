# ML_Toolkit

Final project for CS1660 Intro to Cloud Computing

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
2. Either build the images yourself, or pull them from my dockerhub.

**Build yourself** 

```bash
cd ML_Toolkit
docker-compose build
docker-compose up
```

**Use Dockerhub**
```bash
cd ML_Toolkit
docker-compose -f dockerhub.yml up
```
3. Open any web browser to `http://localhost/main.html`
4. For subsequent runs, be sure to run `docker-compose down` before running `docker-compose up`

### Regards
- Tableau, Sonarscanner, Hadoop, and Spark may take an extra minute to start up
- Tableau needs a license to activate it
- Tableau login - username: tableau | password: tableau
- Dockerhub - https://hub.docker.com/repository/docker/noah710/ml_toolkit

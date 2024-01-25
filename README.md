# Docker Deployment with Unix Socket

### This demo project features a containerized deployment with two images:

Note: 
- The 'main' branch contains configurations for a shared volume that utilizes the host machine.
- The 'docker-Unix-socket' branch, on the other hand, does not involve a shared volume with the host machine; instead, all configurations are contained within the Docker container.

## Django Image:

- Contains the Django application.
- Configured to communicate with the Nginx image via a Unix socket.

## Nginx Image:

- Nginx server image serving as a reverse proxy.
- Connected to the Django application using a Unix socket instead of a traditional TCP socket.

## Project Structure:
```bash
/project-root
│
├── django-app
│ ├── ... # Django application files
│ └── uwsgi.ini # uWSGI configuration using a Unix socket
│
└── nginx-config
├── ... # Nginx configuration files
└── default.conf # Nginx configuration specifying connection to the Unix socket

```

## Docker Configuration:

**Django Image:**

- Utilizes uWSGI with a Unix socket. Check `uwsgi.ini` for configuration.
- Exposes the Unix socket at `/path/to/socket/socket.sock`.

**Nginx Image:**

- Configured to communicate with the Django application via the Unix socket.
- Nginx configuration file (`default.conf`) specifies the connection to the Unix socket.

## How to Run:

Run the following command to build the images and start the container:

```bash
docker-compose up --build





# docker_config

## Docker Images:

## Created two Docker images:
Django Image (Dockerfile):

dockerfile
Copy code
```bash

FROM python:3.10-slim-buster
RUN apt update && apt install -y build-essential
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt
CMD ["uwsgi", "app.ini", "--thunder-lock"]
```
Nginx Image (Dockerfile):


dockerfile
Copy code
```bash

FROM nginx
COPY cert_full.pem /etc/nginx/ssl/cert_full.pem
COPY key.key /etc/nginx/ssl/key.key
COPY nginx.conf /etc/nginx/conf.d
Nginx Configuration (nginx.conf):
```
nginx
Copy code
```bash

upstream exampletry {
    server unix:/tmp/app.sock;
}

server {
    listen 90 ssl;
    server_name localweb;

    ssl_certificate /etc/nginx/ssl/cert_full.pem;
    ssl_certificate_key /etc/nginx/ssl/key.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;
    ssl_stapling_verify on;

    location / {
        include uwsgi_params;
        uwsgi_pass exampletry;

        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-Host $host;
        proxy_send_timeout 30s;
    }
}

```

Docker Compose (docker-compose.yml):

yaml
Copy code
```bash

version: '1'
services:
  exampletry:
    build: ./exampletrydoc
    volumes:
      - /tmp

  nginx:
    build: ./nginx
    volumes_from:
      - exampletry
    ports:
      - "90:90"

```
Startup Script (start-docker-compose.sh):

bash
Copy code
```bash

#!/bin/bash
cd /home/dockern/dockerUnixSocket/dockerTry/
sudo docker compose up -d --build
```
Cronjob Setup:

Run crontab -e and add the following line:
bash
Copy code
```bash

@reboot /home/dockern/dockerUnixSocket/dockerTry/start-docker-compose.sh
```
This setup utilizes Docker Compose to manage the deployment of Django and Nginx containers. The cronjob ensures the containers start on system reboot by executing the startup script.






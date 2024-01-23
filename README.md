# Docker Deployment with Unix Socket

### This demo project features a containerized deployment with two images:

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

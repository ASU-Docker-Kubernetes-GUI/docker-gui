# Docker/Kubernetes GUI

The Docker/Kubernetes GUI is designed with simplicity in mind. 
It allows users to perform quick and easy deployments of their Docker/Kubernetes
workflows.

Additionally, it allows users to stream logs and view telemetry data
of their running containers. Allows users to deploy containers
from a graphical user interface without needing to know any Docker/Kubectl
CLI commands.

## Authors
- Ivan Martinez Morales
- Harsha Sidda
- Shubhang Goel
- Harris Mustic

As part of the ASU Computer Science Capstone project

## Setup

Use the provided venv to get started.

```shell script
pip install virtualenv
source venv/bin/activate
```

Then load the needed dependencies

```shell script
pip install -r requirements.txt
```

## Running Locally

To run locally:

```shell script
python app.py
```

## Running with Docker

To run in a Docker container:

```shell script
docker build -t dockernetes:latest .
docker run -r 5000:5000 dockernetes
```

# Docker

Helper commands

docker images
docker ps -a
docker build -t us-central1-docker.pkg.dev/prefab-grid-455104-h7/guessthenumber/guess-the-number-game:v1.5 .
docker push us-central1-docker.pkg.dev/prefab-grid-455104-h7/guessthenumber/guess-the-number-game:v1.5

prefab-grid-455104-h7 = my gcp prject
guessthenumber = docker repo
guess-the-number-game:v1.5 = image name with tag  (use ":latest tag" to be consistent with your deployment)

Use terraform create docker repo (in Artifact registry)
Use terraform to create a cloud run use this image to run your application.

# Guess the Number Game

A simple web-based game where users try to guess a random number between 1 and 100. This project is built using **Flask** and Dockerized for deployment on **Google Cloud Run**.

## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Terraform](https://www.terraform.io/downloads)
- Google Cloud Project with billing enabled.

## Steps to Deploy the Application

### Create an Artifact Registry Docker Repository using Terraform

First, you need to create a Docker repository in Google Artifact Registry to store your image. Here's the Terraform configuration to create the repository:

```hcl
provider "google" {
  project = "prefab-grid-455104-h7"
  region  = "us-central1"
}

resource "google_artifact_registry_repository" "docker_repo" {
  name        = "guessthenumber"
  location    = "us-central1"
  repository_id = "guessthenumber"
  format      = "DOCKER"
}


# Build the Docker image
docker build -t us-central1-docker.pkg.dev/prefab-grid-455104-h7/guessthenumber/guess-the-number-game:v1.5 .

# Push the image to Artifact Registry
docker push us-central1-docker.pkg.dev/prefab-grid-455104-h7/guessthenumber/guess-the-number-game:v1.5

# Create a cloud run service
resource "google_cloud_run_service" "game_service" {
  name     = "guess-the-number-game"
  location = "us-central1"
  project  = "prefab-grid-455104-h7"

  template {
    spec {
      containers {
        image = "us-central1-docker.pkg.dev/prefab-grid-455104-h7/guessthenumber/guess-the-number-game:v1.5"
        ports {
          container_port = 8080
        }
      }
    }
  }

  traffics {
    latest_revision = true
    percent         = 100
  }
}
```

# Play the game
Go to Cloud run in console find the link similar to https://guess-the-number-game-353918041635.us-central1.run.app/


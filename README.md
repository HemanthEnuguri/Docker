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


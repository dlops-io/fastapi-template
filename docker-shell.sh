#!/bin/bash

set -e

# Read the settings file
source ./env.dev

docker build -t $IMAGE_NAME -f Dockerfile .
docker run --rm \
--name $IMAGE_NAME \
-ti \
--mount type=bind,source="$BASE_DIR",target=/app \
-p 9500:9000 \
-e DEV=1 \
$IMAGE_NAME
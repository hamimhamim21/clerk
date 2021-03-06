#!/bin/bash
#
# Deploy clerk the host server
# Run this from the project root
#
HOST='3.106.55.74'

case $CIRCLE_BRANCH in
    "develop")
        export COMPOSE_SUFFIX="staging"
        export PROJECT="clerk_test"
        ;;
    "master")
        export COMPOSE_SUFFIX="prod"
        export PROJECT="clerk"
        ;;
esac


ssh root@$HOST /bin/bash << EOF
    set -e
    echo "Setting up deployment files for $PROJECT"
    mkdir -p /srv/${PROJECT}/
EOF

echo "Copying $PROJECT compose file"
scp docker/docker-compose.${COMPOSE_SUFFIX}.yml root@${HOST}:/srv/$PROJECT

ssh root@$HOST /bin/bash << EOF
    set -e
    echo "Deploying $PROJECT to docker swarm"
    docker stack deploy \
        --compose-file /srv/${PROJECT}/docker-compose.${COMPOSE_SUFFIX}.yml \
        $PROJECT
EOF

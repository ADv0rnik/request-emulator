#!/usr/bin/env bash


cd ..

docker compose -f docker-compose.test.yml -p compose_for_tests up --build -d
sleep 4

# shellcheck disable=SC1072
# shellcheck disable=SC1073
# shellcheck disable=SC1009
# shellcheck disable=SC1020
if [ $? -ne 0]; then
  echo "Error running tests"
  exit 1
fi
  docker logs api-test
  sleep 1
  docker compose -p compose_for_tests down



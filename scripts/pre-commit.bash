#!/usr/bin/env bash

RED='\033[0;31m'
BGreen='\033[1;32m'

echo -e "${BGreen}Running pre-commit hook...${BGreen}"

../../request-emulator/scripts/run-tests.bash

# shellcheck disable=SC1009
# shellcheck disable=SC1073
# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
  echo -e "${RED}WARNING: Tests must pass before commit ! ${RED}"
  exit 1
fi



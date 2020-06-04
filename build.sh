#!/usr/bin/env bash

# Copyright 2018 JanusGraph Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Defaults
docs=true
build=true
declare -r ENV_NAME=tempENV

while getopts ":d:b:p:" opt; do
  case "${opt}" in
    d)
      docs=$OPTARG
      ;;
    b)
      build=$OPTARG
      ;;
    p)
      export PYTHON_PATH=$OPTARG
      ;;
    \?)
      echo "Usage $0 -d [Build Docs?] -b [Build Lib?] -p [Python Executable Path]"
      exit 1
      ;;
  esac
done

if [[ -z "${1:-}" ]]; then
  echo "Usage $(basename $0) -d [Build Docs?] -b [Build Lib?] -p [Python Executable Path]"
  echo "Building with defaults $0 -d true -b true -p (default python)"
fi

if [[ -z "${PYTHON_PATH+x}" ]]; then
  # If -p parameter isn't provided, we check if pre perquisite python is installed or not.
  if command -v python3 --version &>/dev/null; then
    export PYTHON_PATH=python3
  else
    echo "python3 command doesn't work. Exiting"
    exit 1
  fi
fi

if ! command -v virtualenv --version &>/dev/null; then
  echo "Pre-requisite virtualenv isn't installed on system. Please see docs for help in installation of pre-requisites"
  exit 1
fi

virtualenv -p "${PYTHON_PATH}" "${ENV_NAME}"
echo "Created virtualenv with -p=${PYTHON_PATH}"

# Set the constants needed for this project
source constants.sh

echo "Sourced constants from constants.sh"
echo "Building library with python " $(python -V)

chmod +x before-script.sh
./before-script.sh "${ENV_NAME}"

if [[ "${docs}" == "true" ]]; then
  echo "Building documentation"
  chmod +x build-docs.sh
  {
    ./build-docs.sh "${ENV_NAME}"
  } || {
    echo "Docs build failed. Exiting build"
    exit -1
  }
fi

if [[ "${build}" == "true" ]]; then
  echo "Building library"
  chmod +x build-library.sh
  {
    ./build-library.sh "${ENV_NAME}"
  } || {
    echo "Exiting build as library build failed"
    exit -1
  }
fi

# Remove all files for temp environment, as that is already deactivated
rm -rf "${ENV_NAME}"
echo "Removed ${ENV_NAME}"

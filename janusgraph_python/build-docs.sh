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


if [ -z "${1:-}" ]; then
  echo "Usage $(basename $0) [Env Name]"
  exit 1
else
  ENV_NAME="${1}"
fi

case $(uname -s) in
  MINGW*)     python_path="${ENV_NAME}"/Scripts/activate;;
  *)          python_path="${ENV_NAME}"/bin/activate
esac
#
source "${python_path}"
#pyenv activate "${ENV_NAME}"

# Auto-generate .rst files from docstrings of Python files. The .rst files are then used to generate html files
# for API docs
sphinx-apidoc -o docs/ src/main/python/janusgraph_python > /dev/null
# Generate HTML files from .rst files
pyb sphinx_generate_documentation

cd docs

# Remove auto-generated files to keep git history cleaner. They are anyways added to .gitignore also.
rm -rf janusgraph_python*.rst
rm -rf modules.rst

cd ../

#pyenv deactivate

case $(uname -s) in
    MINGW*)     source deactivate;;
    *)          deactivate
esac

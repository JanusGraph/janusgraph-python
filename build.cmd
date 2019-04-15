@echo off

REM Copyright 2018 JanusGraph Python Authors

REM Licensed under the Apache License, Version 2.0 (the "License");
REM you may not use this file except in compliance with the License.
REM You may obtain a copy of the License at

    REM http://www.apache.org/licenses/LICENSE-2.0

REM Unless required by applicable law or agreed to in writing, software
REM distributed under the License is distributed on an "AS IS" BASIS,
REM WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
REM See the License for the specific language governing permissions and
REM limitations under the License.

set %1
set %2

set docs=%d%
set build=%b%
set ENV_NAME=tempENV

IF NOT DEFINED docs IF NOT DEFINED build (
    echo Invalid usage of build file. Usage: build.cmd "d=true" "b=true"
    exit /b %errorlevel%
)

python --version >nul 2>&1 && (
    echo prerequisite Python is installed.
) || (
    echo Python not installed. Please refer to docs to install Python, which is prerequisite for building this lib.
    exit /b %errorlevel%
)

virtualenv --version >nul 2>&1 && (
    echo Pre-requisite virtualenv installed
) || (
    echo Please install the pre-requisite virtualenv before continuing.
    exit /b %errorlevel%
)

virtualenv %ENV_NAME%

call %ENV_NAME%\Scripts\activate

python -m pip install pybuilder >nul
echo Installed PyBuilder
python -m pip install sphinx >nul
echo Installed Sphinx

call deactivate

if /I %docs% == true (
    echo Building Docs
    call %ENV_NAME%\Scripts\activate

    sphinx-apidoc -o docs src\main\python\janusgraph_python >nul
    echo Generated API Docs

    pyb_ sphinx_generate_documentation -v
    echo Build HTML Docs

    cd docs\

    for %%A in (janusgraph_python*.rst) do del /F /Q "%%A"
    del /F /Q modules.rst

    cd ..\

    call deactivate
)

if /I %build% == true (
    echo Building Library
    call %ENV_NAME%\Scripts\activate

    pyb_ -v
    echo JanusGraph-Python successfully build

    call deactivate
)

rmdir /S /Q %ENV_NAME%

pause

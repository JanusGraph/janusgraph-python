# Building JanusGraph client for Python

- Building Library:

A set of scripts have been created to make the job of building the library easier for user, but the scripts
expects few pre requisites to be installed before hand. 

- Pre-Requisites:
    - Python needs to be installed on system. The library is currently tested against Python
    3.4, 3.5 & 3.6 only.
    
    - Python is added to system path. Make sure, the user can run the following commands from command line:
        - python3/ python3.4/ python3.5/ python3.6 on Unix machines.
        - python on Windows machines.
        
    - Virtualenv needs to be installed. See [PyPi Page](https://pypi.org/project/virtualenv/) for installation steps.
    
    - The automated build scripts are tested on following Operating Systems:
        - Windows 7
        - CentOS
        - RHEL 7
        - Ubuntu 18.04
        - MacOS
        
- Building on Windows 7:
    - A script build.cmd is created which accepts following keyword arguments:
        - `d`: Specifies whether documents to be build. Set to true or false.
        - `b`: Specifies whether library to be build. Set to true or false.
    
    - If any of parameters are missing, the script exits with error message. 
    An appropriate way to invoke the script would be:
        ```bash
        build.cmd "d=true" "b=true"
        ```
    - The above example builds the docs, library and also installs to local global Python site-packages.

- Building on Unix System:
    - A script named build.sh is created which accepts following parameters:
        - `-d`: Default to true. Specifies if documentation is to be build.
        - `-b`: Defaults to true. Specifies if library is to be build.
        - `-p`: The path to Python interpreter on system. If not provided, the script expects python3 is installed\
         and the command python3 works on shell and is used to generate virtualenv. If provided, the provided path is \
         used to generate virtualenv.
        
    **NOTE**: If you are building library on Max OS (OSx), then you will need to run by pre pending sudo -H. 
    Eg: sudo -H ./build.sh
    
    If any of the defaults needs to be changed, the parameter needs to be specified explicitly while running the script.
    
    - If you want to build just the documentation, without the library.
        ```bash
        ./build.sh -b false
        ```
        
    - If you want to build just the library but aren't interested in building docs.
        ```bash
        ./build.sh -d false
        ```
        
    - If you just want to build the library, and you have python interpreter installed at /usr/lib/python
        ```bash
        ./build.sh -d false -p /usr/lib/python
        ```
        
    - And so on depending on your requirements.

Once done,
    - You can see the built HTML files under `docs/_build/index.html` directory.
    - You can see the build library under `target/dist/janusgraph-python/dist` directory.

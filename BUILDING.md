# Building JanusGraph client for Python

-   Building Library:

    A set of scripts have been created to make the job of building the library easier for user, but the scripts
    expects few pre requisites to be installed before hand. 

-   Pre-Requisites:

    -   Python needs to be installed on system. The library is currently tested against Python
        3.4, 3.5, 3.6, 3.7 and 3.8

    -   Python is added to system path. Make sure, the user can run the following commands from command line:
        -   python3/ python3.4/ python3.5/ python3.6 / python3.7 / python3.8 on Unix machines.
        -   python on Windows machines.
        
    -   Make sure following (specific to version of python version installed) works:
        -   python3 --version
        -   python3.4 --version
        -   python3.5 --version
        -   python3.6 --version

    -   Virtualenv needs to be installed. See [PyPi Page](https://pypi.org/project/virtualenv/) for installation steps.

    -   The automated build scripts are tested on following Operating Systems:
        -   Windows 7
        -   CentOS
        -   RHEL 7
        -   Ubuntu 18.04
        -   Ubuntu WSL
        -   MacOS

-   Building on Windows 7:

    -   A script build.cmd is created which accepts following keyword arguments:
        -   `d`: Specifies whether documents to be build. Set to true or false.
        -   `b`: Specifies whether library to be build. Set to true or false.

    -   If any of parameters are missing, the script exits with error message. 
        An appropriate way to invoke the script would be:
        ```bash
        build.cmd "d=true" "b=true"
        ```

    -   The above example builds the docs, library and also installs to local global Python site-packages.

-   Building on Unix System:

    -   A script named build.sh is created which accepts following parameters:

        -   `-d`: Default to true. Specifies if documentation is to be built.
        
        -   `-b`: Defaults to true. Specifies if library is to be built.
        
        -   `-p`: The path to Python interpreter on system. If not provided, the script expects python3 is installed
             and the command python3 works on shell and is used to generate virtualenv. If provided, the provided path is 
             used to generate virtualenv.

        **NOTE**: If you are building library on Max OS (OSx), then you will need to run by pre pending `sudo -H`. 
        Eg: `sudo -H ./build.sh`

        If any of the defaults needs to be changed, the parameter needs to be specified explicitly while running the script.
    
    -   If you want to build just the documentation, without the library.
        ```bash
        ./build.sh -b false
        ```
        
    -   If you want to build just the library but aren't interested in building docs.
        ```bash
        ./build.sh -d false
        ```
        
    -   If you just want to build the library, and you have python interpreter installed at /usr/lib/python
	
        ```bash
        ./build.sh -d false -p /usr/lib/python
        ./build.sh -d false -p python3.6
        ```
        
    -   And so on depending on your requirements.

    Once done,
    -   You can see the built HTML files under `docs/_build/index.html` directory.
    -   You can see the build library under `target/dist/janusgraph-python/dist` directory.


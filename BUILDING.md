# Building JanusGraph-Python

## Requirements

* [Python 3.9][python39] or newer is needed to run the project.
* [Docker][docker] needs to be running in order to execute the integration tests as they automatically start a JanusGraph Docker container.
* [pytest][pytest] and [testcontainers][testcontainers] are needed to test the project.

## Test

The library can be tested by executing:

```sh
pip install -r requirements.txt
pip install -r tests/requirements.txt

python -m pytest
```

The library can be packed into PyPI package by executing:

```sh
pip install build

python -m build
```

[python39]: https://www.python.org/downloads/release/python-390/
[docker]: https://www.docker.com/
[pytest]: https://docs.pytest.org/
[testcontainers]: https://pypi.org/project/testcontainers/

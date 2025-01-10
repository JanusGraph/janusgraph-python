from setuptools import setup
from pathlib import Path
from os.path import isfile, join

this_directory = Path(__file__).parent
requirements_path = join(this_directory, 'requirements.txt')

def read_requirements(path):
    install_requires = []

    if isfile(path):
        with open(path) as f:
            install_requires = [line for line in map(str.strip, f.read().splitlines()) if len(line) > 0 and not line.startswith('#')]

    return install_requires
    
install_requires = read_requirements(requirements_path)

setup(
    name='janusgraphpython',
    version='1.1.1',
    description='JanusGraph-Python extends Apache TinkerPop™''s Gremlin-Python with support for JanusGraph-specific types.',
    long_description=(this_directory/'README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://janusgraph.org/',
    author='JanusGraph',
    license='Apache 2',
    packages=['janusgraph_python', 'janusgraph_python.driver',
                   'janusgraph_python.process', 'janusgraph_python.structure',
                'janusgraph_python.structure.io'],
    zip_safe=False,
    data_files=[('', ['LICENSE.txt', 'DCO.txt', 'CC-BY-4.0.txt', 'APACHE-2.0.txt', 'requirements.txt'])],
    test_suite='tests',
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ]
)
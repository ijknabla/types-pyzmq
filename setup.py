from setuptools import setup

setup(
    name="types-pyzmq",
    version="0.0.0",
    packages=["zmq-stubs"],
    package_data={
        "zmq-stubs": ["*.pyi"],
    },
    install_requires=[
        "pyzmq",
    ],
)

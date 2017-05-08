from setuptools import setup

setup(
    name="pystae",
    packages=["pystae"],
    install_requires=["pandas", "requests", "joblib"],
    test_suite='tests'
)

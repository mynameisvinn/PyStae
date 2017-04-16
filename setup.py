from distutils.core import setup

setup(
    name="pystae",
    version="0.1.0",
    packages=["pystae"], # source code folder

    # Include additional files into the package
    include_package_data=True,

    # Details
    # url="http://pypi.python.org/pypi/MyApplication_v010/",

    # Dependent packages (distributions)
    install_requires=[
        "pandas", "requests"
    ],
)

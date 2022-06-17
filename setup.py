import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="qsolve",
    version="0.1.1",
    author="Jan-Frederik Mennemann",
    author_email="jfmennemann@gmx.de",
    # description="",
    # long_description=read('README.md'),
    # long_description=long_description,
    # license="MIT",
    keywords="ultracold atoms, simulations, Gross-Pitaevskii, thermal state sampling, time of flight",
    # url = "http://packages.python.org/an_example_pypi_project",
    # package_dir={'':'qsolve'},
    packages=setuptools.find_packages(),
    # packages=['qsolve'],
    package_data={"qsolve/core": ['qsolve_core.cpython-39-x86_64-linux-gnu.so']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: POSIX :: Linux",
        "Environment :: GPU :: NVIDIA CUDA :: 10.2"
    ],
)


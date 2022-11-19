import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="broadcast_service",
    version="1.1.1",
    author="Zeeland",
    author_email="zeeland@foxmail.com",
    description="A lightweight third-party broadcast library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Undertone0809/broadcast-service",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    keywords="broadcast, broadcast-service",
)

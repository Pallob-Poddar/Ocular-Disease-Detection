from setuptools import setup, Extension
from setuptools import find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="model",
        version = "1.1",
        description="Model: Collection of models",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Pallob Poddar",
        author_email="pallob.poddar@northsouth.edu",
        url="https://github.com/PallobPoddar/Ocular-Disease-Detection",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
        install_requires=["scikit-learn>=0.22.1"],
    )

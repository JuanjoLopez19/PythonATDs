
import io,sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    # Clase personalizada para integrar PyTest en setup.py
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Importa aquí, porque fuera es más difícil gestionar dependencias
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def readme():
    with io.open("README.md", encoding="utf-8") as f:
        return f.read()


def requirements(filename):
    reqs = list()
    with io.open(filename, encoding="utf-8") as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name="ATD_python",
    version="1.0",
    packages=find_packages(),
    url="https://github.com/JuanjoLopez19/PythonATDs",
    download_url="https://github.com/JuanjoLopez19/PythonATDs",
    license="LICENSE.md",
    author="JuanjoLopez19",
    author_email="juanjoselopez@usal.es",
    description="",
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requirements(filename="requirements.txt"),
    data_files=[],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3",
    project_urls={
        "Bug Reports": "https://github.com/JuanjoLopez19/PythonATDs",
        "Source": "https://github.com/JuanjoLopez19/PythonATDs",
    },
)
from setuptools import setup, find_packages

setup(
    name="cherrypy_jinja2",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Jinja2',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)

import os
import sys
from setuptools import setup

# --- version check ---
CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)
if CURRENT_PYTHON < REQUIRED_PYTHON:
    print(
f"""
--- Unsopported Python version ---
pyonos requires at least Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]},
but you're trying to install it on Python {CURRENT_PYTHON[0]}.{CURRENT_PYTHON[1]}.
"""
)
    sys.exit(1)

# --- publish option ---
if sys.argv[-1] == 'publish':
    """pack and publish"""
    os.system('python setup.py sdist bdist_wheel')
    os.system('python -m twine upload dist/*')
    sys.exit()

# --- read readme.md ---
with open("README.md", "r") as f:
    readme = f.read()

# --- setting up ---
setup(
    name="pyonos",
    version='0.1.0',
    author="aaronlyy (Aaron Levi)",
    author_email="<aaronlevican@gmail.com>",
    url="https://github.com/aaronlyy/pyonos",
    description='Wrapper around the IONOS DNS, Domains & SSL API.',
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=["pyonos"],
    install_requires=['requests'],
    keywords=['dns', 'ssl', 'domain', 'domains', 'ipv4', 'ipv6', 'txt', 'cname', 'api', 'ionos'],
    classifiers=[
        "Intended Audience :: Developers",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
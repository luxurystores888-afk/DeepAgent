#!/usr/bin/env python3
"""
DeepAgent v1.0.0 Setup Configuration
====================================

A standalone, open-source AI/ML assistant with multilingual support
for natural language requests in English, Arabic, and Arabizi.

Features:
- Automated ML pipeline execution
- Advanced natural language processing
- Secure credential-based private use
- No dependency on external services
- Modern web interface with search bar
- Complete ML algorithm suite

Author: DeepAgent Team
License: MIT
Repository: https://github.com/luxurystores888-afk/DeepAgent
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from requirements.txt
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="deepagent",
    version="1.0.0",
    author="DeepAgent Team",
    author_email="contact@deepagent.dev",
    description="Standalone AI/ML Assistant with Multilingual Support and Automated ML Pipelines",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/luxurystores888-afk/DeepAgent",
    project_urls={
        "Bug Tracker": "https://github.com/luxurystores888-afk/DeepAgent/issues",
        "Documentation": "https://github.com/luxurystores888-afk/DeepAgent#readme",
        "Source Code": "https://github.com/luxurystores888-afk/DeepAgent",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Text Processing :: Linguistic",
        "Natural Language :: English",
        "Natural Language :: Arabic",
    ],
    packages=find_packages(),
    py_modules=["deepagent"],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "pre-commit>=2.20",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.18",
        ],
        "gpu": [
            "tensorflow-gpu>=2.10.0",
            "torch-gpu>=1.12.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "deepagent=deepagent:main",
            "deepagent-server=deepagent:run_server",
            "deepagent-cli=deepagent:cli_interface",
        ],
    },
    include_package_data=True,
    package_data={
        "deepagent": [
            "templates/*.html",
            "static/*.css",
            "static/*.js",
            "models/*.pkl",
            "data/*.json",
        ],
    },
    keywords=[
        "ai", "ml", "machine-learning", "artificial-intelligence",
        "nlp", "natural-language-processing", "multilingual",
        "english", "arabic", "arabizi", "assistant", "automation",
        "flask", "web-app", "standalone", "open-source"
    ],
    zip_safe=False,
)

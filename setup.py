"""
Setup script for Ayatul Kursi package.
Uses pyproject.toml for configuration via setuptools.
"""

from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    package_data={
        "ayatulkursi": ["assets/*"],
    },
)

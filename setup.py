from setuptools import setup, find_packages

setup(
    name="socialagent",
    version="0.4",
    packages=find_packages(),
    install_requires=[],
    author="Moh Iqbal Hidayat",
    author_email="iqbalmh18.dev@gmail.com",
    description="socialagent is a Python module designed for generating user agents specific to social media platforms under Meta (formerly Facebook).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iqbalmh18/socialagent",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

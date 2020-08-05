import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="learning-locker-sdk-todomac", # Replace with your own username
    version="0.0.1",
    author="todomac",
    author_email="td_mcleod@hotmail.com",
    description="SDK for working with the learninglocker API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="ssh://git@github.com:futureamp/learning_locker_sdk.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
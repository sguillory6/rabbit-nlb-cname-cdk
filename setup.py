import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="basicmq",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "the_basic_mq"},
    packages=setuptools.find_packages(where="the_basic_mq"),

    install_requires=[
        "aws-cdk-lib>=2.24.0",
        "constructs>=10.1.7",
        "python-benedict>=0.25.1"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)

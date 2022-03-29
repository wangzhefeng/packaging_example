import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-wangzhefeng",
    version="0.0.1",
    author="wangzhefeng",
    author_email="wangzhefengr@163.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangzhefeng/example-pkg-wangzhefeng",
    project_urls={
        "Bug Tracker": "https://github.com/example-pkg-wangzhefeng/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
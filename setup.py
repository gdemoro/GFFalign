import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Gffalign", # Replace with your own username
    version="0.5.1",
    author="Gianluca De Moro",
    author_email="gmoro@ualg.pt",
    description="Tool to extract genes coordinates from a whole genome alignent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gdemoro/gffalign",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'gffalign = GFFalign.__main__:main'
        ]
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
          'gffutils',
          'biopython',
    ],
)

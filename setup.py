import setuptools


setuptools.setup(
    name="ctrlf",
    version="0.0.1",
    author="theunderdog",
    author_email="ahmedbonumstelio@gmail.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts':['ctrlf=ctrlf.command:command_main']
        }
)

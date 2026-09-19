from setuptools import find_packages, setup

setup(
    name="smart-calculator",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["main"],
    install_requires=["PySimpleGUI>=5.0"],
    entry_points={
        "console_scripts": [
            "smart-calculator=main:run",
        ],
    },
    python_requires=">=3.10",
)

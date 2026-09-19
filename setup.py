from pathlib import Path

from setuptools import find_packages, setup


ROOT_DIR = Path(__file__).parent


setup(
    name="smart-calculator",
    version="1.0.0",
    description=(
        "A modular calculator with basic, advanced, and "
        "statistical operations."
    ),
    long_description=(ROOT_DIR / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
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

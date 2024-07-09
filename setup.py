from setuptools import setup, find_packages

setup(
    name="sentiment_intention_analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "configparser"
    ],
    entry_points={
        "console_scripts": [
            "analyze=src.functions:main",
        ],
    },
    description="Analyzer to get user and agent dialogs' sentiments and intents",
    package_data={
        "": ["data/*.json", "config/*.ini"]
    },
    include_package_data=True,
)

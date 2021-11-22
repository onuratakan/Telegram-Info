import os
import setuptools


def requirements(file="requirements.txt"):
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []


def readme(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf8") as r:
            return r.read()
    else:
        return ""


setuptools.setup(
    name="TelegramInfo",
    version="1.0.1",
    description="Telegram user and chat information extractor",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/FayasNoushad/Telegram-Info",
    download_url="https://github.com/FayasNoushad/Telegram-Info/releases/latest",
    license="MIT",
    author="Fayas Noushad",
    author_email="contact@fayas.me",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Tracker": "https://github.com/FayasNoushad/Telegram-Info/issues",
        "Source": "https://github.com/FayasNoushad/Telegram-Info",
        "Documentation": "https://telegram-info.projects.fayas.me",
    },
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements()
)

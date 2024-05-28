# Minecraft Fabric Mod Downloader

## Description
This project is a Python-based Minecraft mod downloader that allows users to easily download and install fabric mods for the game using webscraping of the popular Minecraft mod websites curseforge and modrinth.

## Prerequisites
Before getting started, make sure you have the following installed on your system:
- [Python](https://www.python.org/) (version 3.8 or higher)
- [Google Chrome](https://www.google.com/chrome/) browser
- [ChromeDriver](https://chromedriver.chromium.org/downloads) for your specific version of Chrome

## Dependencies
This project requires the following Python libraries:

- `requests`
- `selenium`
- `PyYAML`

## Usage
1. Download the Prerequisites and define the paths to Chrome and ChromeDriver in config.yml
2. Download the Dependencies
3. Edit config.yml for your preferences and mods (config.yml contains an example configuration)
4. Run main
```bash
python main.py
```
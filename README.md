# YTViewer

## Description

**YTViewer** is simple YouTube views bot

## Prerequisites

### Windows

Install Python: https://www.python.org/downloads/

Install required libraries:

```
$ python -m pip install -r requirements.txt
```

Download **ChromeDriver** and move the executable to folder in your PATH: http://chromedriver.chromium.org/downloads

Install **Google Chrome Browser**: https://www.google.com/chrome/

### Linux

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install chromium python -y
$ python -m pip install -r requirements.txt
```

### MacOS

```
$ brew update && brew upgrade
$ brew install python
$ python -m pip instal -r requirements.txt
```

## Installation

Clone this repository:

`$ git clone "https://github.com/DeBos99/ytviewer.git"`

## Usage

Show help:

`$ main.py --help`

Run bot on **URL**:

`$ main.py --url URL`

Set number of threads to **T** (default: 15):

`$ main.py --url URL threads T`

Set duration of view to **S** seconds (default: 300 (5 minutes)):

`$ main.py --url URL --duration S`

Set proxies filepath to **PATH** (default: proxies loaded from web)

`$ main.py --url URL --proxies PATH`

## Authors

* **Michał Wróblewski** - Main Developer - [DeBos99](https://github.com/DeBos99)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

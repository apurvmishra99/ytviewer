# YTViewer

**YTViewer** is simple YouTube views bot

## Prerequisites

### Windows

Install Python: https://www.python.org/downloads/

Install required libraries:

`$ pip install -r requirements.txt`

Download **ChromeDriver** and move the executable to folder in your **PATH**: http://chromedriver.chromium.org/downloads

Install **Google Chrome Browser**: https://www.google.com/chrome/

### Linux

#### APT

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install chromium python -y
$ pip install -r requirements.txt
```

Or

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install chromium python python-setuptools -y
$ sudo easy_install $(cat requirements.txt)
```

#### Pacman

```
$ sudo pacman -Syu --noconfirm
$ sudo pacman -S chromium python --noconfirm
$ pip install -r requirements.txt
```

Or

```
$ sudo pacman -Syu --noconfirm
$ sudo pacman -S chromium python python-setuptools --noconfirm
$ sudo easy_install $(cat requirements.txt)
```

### MacOS

```
$ brew update && brew upgrade
$ brew install python
$ pip instal -r requirements.txt
```

## Installation

Clone this repository:

`$ git clone "https://github.com/DeBos99/ytviewer.git"`

## Usage

Show help:

`$ python main.py --help`

Set url of the video to **URL**:

`$ python main.py --url URL`

Set number of the threads to **T** (default: 15):

`$ python main.py --url URL --threads T`

Set the duration of video in seconds to **S** (default: 300 seconds (5 minutes)):

`$ python main.py --url URL --duration S`

Set the path of proxies list to **PATH** (default: proxies loaded from web):

`$ python main.py --url URL --proxies PATH`

Set the user agent for the driver to **AGENT** (default: randomly generated user agent):

`$ python main.py --url URL --user-agent AGENT`

Set the path of the list of the user agents for the driver to **PATH**:

`$ python main.py --url URL --user-agents PATH`

## TODO

* Add support for **Mozilla Firefox**.
* Add autamatic video duration.
* Add support for multiple urls.

## Authors

* **Michał Wróblewski** - Main Developer - [DeBos99](https://github.com/DeBos99)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

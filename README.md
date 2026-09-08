# Python Practice Repository

A personal collection of Python practice programs, experiments, learning notes, and small utilities. The numbered scripts are independent exercises rather than one application.

## Contents

- `p1.py` through `p62.py` - exercises covering Python fundamentals, problem solving, lists, matrices, strings, recursion, and number properties.
- `music_server.py` - an MCP server that searches the iTunes Search API for music.
- `Timer app with ui.py` - placeholder for a timer UI experiment.
- `test case.py` and `Test.py` - small testing and API experiments.
- `spoken/` - a self-contained static video-learning website with its HTML, CSS, JavaScript, subtitles, and media resources.
- PDF files - personal Python, data structures, Matplotlib, and Tkinter study material.

## Requirements

- Python 3.10 or newer is recommended.
- Most numbered exercises use only the Python standard library.
- `music_server.py` additionally requires the `requests` and `mcp` packages and an internet connection.

## Setup

Create and activate a virtual environment from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies for the music server only when you need it:

```powershell
python -m pip install requests mcp
```

## Running Exercises

Run any exercise directly with Python. Many scripts prompt for input:

```powershell
python .\p1.py
python .\p26.py
python .\p37.py
```

The scripts are standalone, so inspect the file first when choosing an exercise. A few scripts are intended to be imported or extended instead of run directly.

## Music MCP Server

`music_server.py` exposes a `search_music` tool through the Model Context Protocol. It queries the public iTunes Search API and returns song and album names.

Start it with:

```powershell
python .\music_server.py
```

The server expects an MCP-compatible client to connect to it. The API request is made over the internet, and the search term and result limit are supplied by the client.

## Static Website

Open `spoken\index.html` in a browser to explore the included static website. The site uses local HTML, CSS, JavaScript, subtitles, and media resources, so no Python server is required for basic viewing.

## Project Notes

This repository is intentionally exploratory. File names and code style vary between exercises, and some files may be incomplete experiments. Treat each script as a small learning example and run it in isolation.

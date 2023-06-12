# StudyBuddy

## Overview
This repository houses a robust personal assistant built with Python. The personal assistant, inspired by real-world applications like Google Assistant and Siri, provides a suite of features to assist with tasks such as file organization, web search, citation generation, URL shortening, and more.

## Motivation
The project began as an initiative to develop a personal tool to simplify daily tasks, particularly for college students. The motivation behind the project was to create a one-stop solution to handle various tasks and ease the management of various digital resources. Over time, the personal assistant has evolved into a powerful utility capable of multiple functions.

## Features
The personal assistant includes the following features:<br />

**File Organizer:** Helps organize files in your directories based on their extensions.<br />
**Google Search:** Perform a google search directly from the terminal and open the results in the browser.<br />
**Scheduled Google Search:** Schedule a Google search for a specific time of the day.<br />
**Filtered Google Search:** Perform a Google search with filters like site, file type, etc.<br />
**Keyword Alert:** Get an alert when specific keywords appear on given webpages.<br />
**Citation Generator:** Generate citations for books, papers, webpages, images, and videos in MLA, APA, Chicago, Turabian, and IEEE formats.<br />
**URL Shortener:** Shorten long URLs to easily shareable forms.<br />

## Languages and Libraries Used
This project is primarily built with Python. The libraries used in this project include:<br />

**os:** To perform file and directory operations<br />
**webbrowser:** To open a web browser with a specific URL<br />
**requests:** To perform HTTP requests to retrieve webpage content<br />
**BeautifulSoup:** To parse HTML content for the citation generator and keyword alert features<br />
**pyshorteners:** To create shortened URLs<br />

## Installation
To install and run the Personal Assistant, you will need to have Python installed on your machine. Once Python is installed, you can clone this repository, navigate into the project directory and install the required packages using pip.

```
git clone https://github.com/HamzaShili65/PersonalAssistant.git
cd PersonalAssistant
pip install -r requirements.txt
```

Then, you can run the program using Python.

```
python main.py
```

## Future Plans
The next steps for this project include integrating Natural Language Processing (NLP) capabilities into the personal assistant. This will allow the assistant to understand and respond to user commands given in natural language, significantly enhancing its user-friendliness and capability.

## Contribution
Feel free to fork the project and submit pull requests for any features you think would be beneficial. Please adhere to the general coding style of the project and include comments where necessary.

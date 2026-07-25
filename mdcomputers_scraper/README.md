# MDComputers Product Scraper

## Description
This Python script scrapes product details from MDComputers based on a user-provided search term.

## Features
- Accepts a search term as input.
- Opens MDComputers search page using Selenium.
- Extracts:
  - Product Name
  - Price
  - Product Link
- Saves data into `output.csv`.

## Technologies Used
- Python
- Selenium
- Pandas
- WebDriver Manager

## Installation

```bash
pip install selenium pandas webdriver-manager
```

## Run

```bash
python scraper.py
```

Example:

```
Enter product to search:
external harddrive
```

Output:

```
output.csv
```
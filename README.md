# Scrap_with_Selenium
Let's dive deeper into the domain of web scraping using Selenium. This repository leverage automation tool selenium to scrap web pages and later on use Beautiful Soup to parse HTML files to fetch specific elements of concern.

### Table of Contents
-  [Resources](https://github.com/pb319/Scrap_with_Selenium/edit/main/README.md#resource) 
-  [Objective](https://github.com/pb319/Scrap_with_Selenium/edit/main/README.md#objective)
-  [Approach](https://github.com/pb319/Scrap_with_Selenium/edit/main/README.md#approach)
-  [Output Files](https://github.com/pb319/Scrap_with_Selenium/edit/main/README.md#output-files)

#### Resource:
- Youtube Video Link: [Click Here](https://www.youtube.com/watch?v=XI5_nsClCYI&t=197s)
- Tech Stack: `Selenium`, `Beautiful Soup`, `Pandas`
- Selenium Getting Started: [Selenium](https://selenium-python.readthedocs.io/getting-started.html)
- Beautiful Soup: [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start)

#### Objective:
- Create a database of laptops available on `amazon.in`.

#### Approach:
- Export HTML formatted search results one by one from all available pages in the local machine.
- Fetch multiple elements (`title, price, link`) from the HTML files.
- Finally export it as a CSV formatted file.

#### Output Files:
-  [Python Script](https://github.com/pb319/Scrap_with_Selenium/blob/main/collect.py)
-  [HTML Files](https://github.com/pb319/Scrap_with_Selenium/tree/main/Data)
-  [CSV File](https://github.com/pb319/Scrap_with_Selenium/blob/main/data.csv)

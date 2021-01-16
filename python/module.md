# daytime

```py
  import datetime
  today = datetime.now()
  today1 = strftime("%Y%m%d")
  yesterday = datetime(year=2020, month=12, day=31)
  # output format "20201231"
  # https://www.w3schools.com/python/python_datetime.asp
```

# pprint ====> pretty print

```py
from pprint import pprint
pprint(response.json()["prices"])
# outpupt:
  [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
  {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},
  {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},
  {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 551},
  {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},
  {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},
  {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},
  {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},
  {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378}]
```

# Beaufiful soup ==> Web scraping

- Legal
  - You can't Commercialise Copyrighted Content
  - You Can't Scrape Data Behind Authentication
  - You can scrape data without log in
- Ethics

  - Public API First
  - Respect the Web Owner
  - root url/robots.text tells the policy of scraping
    - eg. https://www.linkedin.com/robots.txt
  - crawl-delay: 30
    - not scraping less than one 30 secs
    - recommend to scrap every more than 1 min

- a Python library for pulling data out of HTML and XML files.

```py
  from bs4 import BeautifulSoup
  import lxml

  with open("website.html") as file:
      contents = file.read()

  soup = BeautifulSoup(contents, "html.parser")
  # html.parser may not work for some websites, in such cas, use "lxml" instead.
  # soup = BeautifulSoup(contents, "lxml")
  print(soup.title)   # <title>Angela's Personal Site</title>
  print(soup.title.name)   # the tag name: title
  print(soup.title.string)  # Angela's Personal Site
  print(soup.p)   # The first p tag
  all_anchor_tags = soup.find_all(name="a")   # Find all a tags
  print(all_anchor_tags)

  for tag in all_anchor_tags:
      print(tag.getText())   # Get the text inside <a> tag
      print(tag.get("href"))  # Get href link

  heading = soup.find(name="h1", id="name")   # Get the first h1 tag with id="name"
  print(heading)

  section_heading = soup.find(name="h3", class_="heading")   # Get the first h3 tag with class="heading"
  section_heading.getText()     # get the text content
  section_heading.get("class")  # get class attribute value
  section_heading.name   # Get the tag name, h3

  # Using CSS selector
  company_url = soup.select_one(selector="p a")  # Get the a tag inside p tag
  name = soup.select_one(selector="#name")
  heading = soup.select(".heading")  # return a list: [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]
  print(heading)

  ## with real URL
  response = requests.get("https://news.ycombinator.com/news")
  website_html = response.text   # get the html code of page "https://news.ycombinator.com/news"
  soup = BeautifulSoup(website_html, "html.parser")

```

# Selenium

- installation
  - install chrome
  - install chrome driver https://chromedriver.chromium.org/downloads
    - save the chromedriver into a folder that you won't delete easily
    - copy the chromedirver path to your python file
    - https://www.udemy.com/course/100-days-of-code/learn/lecture/21785302#questions


# time
 - Epoch timestamp is a unit of measurement for time. It is the number of seconds elapsed since the countdown has started. 
 - Beginning epochs per system:
  - macOS - January 1, 1904
  - Windows - January 1, 1601
  - Unix - January 1, 1970

 - time.time()
  - Return the time in seconds since the epoch as a floating point number.
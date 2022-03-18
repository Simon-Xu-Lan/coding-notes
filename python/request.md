# My HTTP Header

- http://myhttpheader.com/

# pass headers with the requests library

- https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method

```py
  r=requests.get("http://www.example.com/", headers={"content-type":"text"})
```

# Request webpage-html from Amazon.

- need headers in request get method
- Add more items in the headers till you get the actual webpage.
  - https://www.udemy.com/course/100-days-of-code/learn/lecture/21709134#questions
  - You'll need to pass along some headers in order for the request to return the actual website HTML. At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header.
  - Print the output of the get request and make sure the actual HTML of the web page is printed, if not try adding more items from your header.

```py
  from bs4 import BeautifulSoup
  import requests

  URL = "https://www.amazon.com/CalDigit-TS3-Plus-Thunderbolt-Dock/dp/B07CZPV8DF/ref=sr_1_18?dchild=1&keywords=usb+station+for+macbook+pro&qid=1609889192&sr=8-18"
  headers = {
      "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
      "X-Http-Proto": "HTTP/1.1",
      "Accept-Encoding": "gzip, deflate",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
  }
  response = requests.get(URL, headers=headers)
  webpage_html = response.text
  # print(webpage_html)
  soup = BeautifulSoup(webpage_html, "html.parser")
  price = soup.find(name="span", id="priceblock_ourprice")
  print(price)
```

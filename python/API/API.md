**API**
# API
- Application Programming Interfaces
- It is a software intermediary that allows systems to communicate with each other. 
- Modern client-to-server communications are mostly handled by APIs.
- is a set of commands, functions, protocols, and objects

  - that programmers can use to
    - create software
    - or interact with an external system

# RESTful API
- REpresentational State Transfer is a terminology that is frequently used to describe APIs.
- It is a framework that describe some best practices for implementing APIs.
- APIs that satisfy the REST principles are recognized as RESTful APIs.


- HTTP Codes

  - 1xx: Hold ON
  - 2XX: Here you Go => successful
  - 3xx: Go away => you don't have permission to access
  - 4xx: You screwed up => something wrong at request side
  - 5XX: I screwed up => something wrong at server side

  - javascript:void(0)

- response

  - response.raise_for_status()
  - response.json()
    - return that json format data
  - response.url

- API Parameters

  - https://api.sunrise-sunset.org/json?lat=39.812990&lng=105.085220

  ```py
    import requests

    MY_LAT = 39.812990
    My_LNG = -105.085220

    parameters = {
        "lat": MY_LAT,
        "lng": My_LNG
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
  ```

  ```py
    import requests

    api_key = "bac6bdea9c179d427565c0bc9f8fc351"
    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

    parameter = {
        "lat": 39.801121,
        "lon": -105.081451,
        "appid": api_key
    }


    response = requests.get(url=OWM_Endpoint, params=parameter)
    response.raise_for_status()
    data = response.json()
    print(data)

  ```

- online json viewer

  - http://jsonviewer.stack.hu/

- API list
  - https://apilist.fun/
  - Stock Price API https://www.alphavantage.co/
    - API Key: WHKNAHNQ03MGQP63
  - News API https://newsapi.org/
    - API Key: 4170118ecad8405790edc56242f6335e
- Twilio API https://www.twilio.com/

```py
  from twilio.rest import Client

  client = Client(account_sid, auth_token)
  message = client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12407527107',
                     to='+17203978719'
                 )
```

- Pixela

- HTTP Requests

  - GET
    requests.get()
  - POST
    requests.post()
  - PUT
    requests.put()
  - DELETE
    requests.delete()

- HTTP headers

  ```py
    graph_endpoint = f"{pixela_endpoint}/simon/graphs"

    graph_config = {
        "id": "graph1",
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }

    headers = {
        "X-USER-TOKEN": "codeforfun2020"
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

  ```

- Nutritionix API

  - https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#

- Google Sheet Data Management
  - Sheety API
  - 100 days of code lecture 330 https://www.udemy.com/course/100-days-of-code/learn/lecture/21309266#overview

- Flight Search API (Free Signup, Requires Credit Card Details) -
  - https://partners.kiwi.com/
  - Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api




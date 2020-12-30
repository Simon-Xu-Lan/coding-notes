**API**

- Application Programming Interfaces
- is a set of commands, functions, protocols, and objects

  - that programmers can use to
    - create software
    - or interact with an external system

- HTTP Codes

  - 1xx: Hold ON
  - 2XX: Here you Go => successful
  - 3xx: Go away => you don't have permission to access
  - 4xx: You screwed up => something wrong at request side
  - 5XX: I screwed up => somthing wrong at server side

  - javascript:void(0)

- response

  - response.raise_for_status()
  - response.json()
    - return that json format data

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

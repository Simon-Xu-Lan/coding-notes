import requests
import json

# Google developer API key
gkey="AIzaSyDV5qmhXKZ9KFQJd5oJlVSNpJzggRlx0Eo"

# Google Geocode

# 1.  Find information by address or city
# Target city
target_city = "Boise, Idaho"

# Build the endpoint URL
target_url = ('https://maps.googleapis.com/maps/api/geocode/json?'
    'address={0}&key={1}').format(target_city, gkey)

geo_data = requests.get(target_url).json()

# 2. Find by places type https://developers.google.com/places/web-service/supported_types



# Google Places


target_coordinates = "43.6187102, -116.2146068"
target_search = "Chinese"
target_radius = 8000
target_type = "restaurant"

# set up a parameters dictionary
params = {
    "location": target_coordinates,
    "keyword": target_search,
    "radius": target_radius,
    "type": target_type,
    "key": gkey
}

# base url
base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# run a request using our params dictionary
response = requests.get(base_url, params=params)
places_data = response.json()
print(places_data["results"][0]["name"])
print(places_data["results"][0]["vicinity"])
# China Grand Buffet
# 10498 W Fairview Ave, Boise

#  Find Place request for "Museum of Contemporary Art Australia",
#  including the photos, formatted_address, name, rating, opening_hours, and geometry fields:

URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
params = {
    "input": "Museum of Contemporary Art Australia",
    "inputtype": "textquery",
    "fields": "photos,formatted_address,name,rating,opening_hours,geometry",
    "key": gkey
}

data = requests.get(URL, params=params).json()
print(data)



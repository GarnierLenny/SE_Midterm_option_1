import urllib.parse
import requests

loc1 = "Wahington, D.C."
loc2 = "Baltimore, Maryland"
api_key=""

def geocoding (location):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1",
    "key": api_key})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200:
        json_data = requests.get(url).json()
        lat=(json_data["hits"][0]["point"]["lat"])
        lng=(json_data["hits"][0]["point"]["lng"])
        country=(json_data["hits"][0]["country"])
    else:
        lat="null"
        lng="null"
    return json_status,country,lat,lng 

start = geocoding("Washington D.C.")
print(start)
end = geocoding("Toronto")
print(end)

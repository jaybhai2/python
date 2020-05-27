import requests

response = requests.get(
    'https://earthquake.usgs.gov/fdsnws/event/1/query',
    params=[('format','geojson'),('starttime','2020-01-01'),('endtime','2020-01-02')]
)

response.json()["features"][0] # convert to json object -> get dict key feature ->return a list 


response = requests.get(
    'https://earthquake.usgs.gov/fdsnws/event/1/count',
    params={'format': 'geojson'},
)

response.json()


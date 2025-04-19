# config.py

SEARCH_CONFIG = {
    "years": [2022, 2023],
    "max_price": 45000,
    "max_mileage": 50000,
    "must_have": ["navigation", "wireless carplay", "awd"],
    "zip_code": "11050",
    "radius_miles": 60
}

EMAIL_CONFIG = {
    "sender": "mattalevy@yahoo.com",
    "receiver": "matt0164@outlook.com",
    "app_password": "aaghptdxzpfetxqi"
}

DEALER_CONFIG = [
    {
        "name": "BMW of Bayside",
        "search_url": "https://www.bmwbayside.com/search/pre-owned-bayside-ny/?cy=11363&tp=pre_owned",
        "lat": 40.758556,  # Bayside, Queens, NY  [oai_citation_attribution:0‡LatLong](https://www.latlong.net/place/bayside-queens-ny-usa-24005.html?utm_source=chatgpt.com)
        "lon": -73.765434
    },
    {
        "name": "Rallye BMW",
        "search_url": "https://www.rallyebmw.com/used-vehicles/",
        "lat": 40.779400,  # 1 Brush Hollow Rd, Westbury, NY  [oai_citation_attribution:1‡MapQuest](https://www.mapquest.com/us/new-york/westbury/11590-2438/1-brush-hollow-rd-40.7794%2C-73.55777?utm_source=chatgpt.com)
        "lon": -73.557770
    },
    {
        "name": "Habberstad BMW of Huntington",
        "search_url": "https://www.habberstadbmwofhuntington.com",
        "lat": 40.828310,  # 230 E Jericho Tpke, Huntington Station, NY  [oai_citation_attribution:2‡MapQuest](https://www.mapquest.com/us/new-york/huntington-station/11746-7341/230-e-jericho-tpke-40.82831%2C-73.40108?utm_source=chatgpt.com)
        "lon": -73.401080
    },
    {
        "name": "Competition BMW of Smithtown",
        "search_url": "https://www.competitionbmw.com/used-vehicles/",
        "lat": 40.877202,  # St. James (599 Middle Country Rd), NY  [oai_citation_attribution:3‡Wikipedia](https://en.wikipedia.org/wiki/St._James%2C_New_York?utm_source=chatgpt.com)
        "lon": -73.155260
    },
    {
        "name": "Rallye Lexus – Glen Cove",
        "search_url": "https://www.rallyelexus.com/used-vehicles/",
        "lat": 40.867222,  # Glen Cove, NY  [oai_citation_attribution:4‡Wikipedia – Die freie Enzyklopädie](https://de.wikipedia.org/wiki/Glen_Cove?utm_source=chatgpt.com)
        "lon": -73.627778
    },
    {
        "name": "Autotrader",
        "search_url": "https://www.autotrader.com/cars-for-sale/all-cars/bmw/530e-xdrive/port-washington-ny?zip=11050",
        "lat": 40.827454,  # Port Washington, NY  [oai_citation_attribution:5‡LatLong](https://www.latlong.net/place/port-washington-ny-usa-31918.html?utm_source=chatgpt.com)
        "lon": -73.699722
    },
    {
        "name": "Carvana",
        "search_url": "https://www.carvana.com/cars/filters?cvnaid=eyJmaWx0ZXJzIjp7Im1ha2VzIjpbeyJuYW1lIjoiQk1XIiwicGFyZW50TW9kZWxzIjpbeyJuYW1lIjoiNSBTZXJpZXMiLCJ0cmltcyI6WyI1MzBlIl19XSwibW9kZWxzIjpbXX1dfX0%3D",
        "lat": None,
        "lon": None
    },
]
"""
Data models for creating new scooters
"""
from datetime import datetime
from datetime import timedelta

now = datetime.now()
end = now + timedelta(minutes=15)
current_time = now.strftime("%H:%M:%S")
end_time = end.strftime("%H:%M:%S")

def scooter_sthlm(name):
    data = {
        "active_user": name,
        "city_location": "Stockholm",
        "lat": 59.202040,
        "lng": 18.023540,
        "start_time": current_time,
        "event": "Simulering för " + name,
        "start_lat": 59.202040,
        "start_lng": 18.023540,
        "end_time": end_time,
        "end_lat": 59.33914,
        "end_lng": 18.07281,
    }
    return data

def scooter_gbg(name):
    data = {
        "active_user": name,
        "city_location": "Göteborg",
        "lat": 57.695320,
        "lng": 11.990840,
        "start_time": current_time,
        "event": "Simulering för " + name,
        "start_lat": 57.695320,
        "start_lng": 11.990840,
        "end_time": end_time,
        "end_lat": 57.411079,
        "end_lng": 11.582159,
    }
    return data

def scooter_malmo(name):
    data = {
        "active_user": name,
        "city_location": "Malmö",
        "lat": 55.421259,
        "lng": 13.112160,
        "start_time": current_time,
        "event": "Simulering för " + name,
        "start_lat": 55.421259,
        "start_lng": 13.112160,
        "end_time": end_time,
        "end_lat": 55.421139,
        "end_lng": 13.11840,
    }
    return data

def scooter_orebro(name):
    data = {
        "active_user": name,
        "city_location": "Örebro",
        "lat": 59.153480,
        "lng": 15.131380,
        "start_time": current_time,
        "event": "Simulering för " + name,
        "start_lat": 59.153480,
        "start_lng": 15.131380,
        "end_time": end_time,
        "end_lat": 59.161920,
        "end_lng": 15.131800,
    }
    return data

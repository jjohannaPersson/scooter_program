"""
Data models for creating new scooters
"""
from datetime import datetime
from datetime import timedelta
import random

now = datetime.now()
end = now + timedelta(minutes=1)
current_time = now.strftime("%H:%M:%S")
end_time = end.strftime("%H:%M:%S")

sthlm_lat_one = 59.341476
sthlm_lat_two = 59.329656
sthlm_lng_one = 18.031697
sthlm_lng_two = 18.123361

def scooter_sthlm(name):
    start_lat = random.uniform(sthlm_lat_one, sthlm_lat_two)
    start_lng = random.uniform(sthlm_lng_one, sthlm_lng_two)
    data = {
        "active_user": name,
        "city_location": "Stockholm",
        "lat": start_lat,
        "lng": start_lng,
        "start_time": current_time,
        "event": "Simulering för " + name,
        "start_lat": start_lat,
        "start_lng": start_lng,
        "end_time": end_time,
        "end_lat": random.uniform(sthlm_lat_one, sthlm_lat_two),
        "end_lng": random.uniform(sthlm_lng_one, sthlm_lng_two),
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

def update_scooter(id, current_lat, current_lng, battery, end_lat, end_lng):
    data = {
        "_id": id,
        "battery": int(battery) - 1,
        "speed": random.randint(5, 20),
        "lat": random.uniform(current_lat, end_lat),
        "lng": random.uniform(current_lng, end_lng)
    }
    return data

def add_10_sec(start_time):
    to_date_time = datetime.strptime(start_time, "%H:%M:%S")

    add_ten = to_date_time + timedelta(seconds=10)
    new_time = add_ten.strftime("%H:%M:%S")

    return new_time

def update_scooter_done(id, battery, speed, lat, lng):
    data = {
        "_id": id,
        "battery": battery,
        "speed": speed,
        "lat": lat,
        "lng": lng
    }
    return data

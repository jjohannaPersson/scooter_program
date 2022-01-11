"""
Data models for creating new scooters
"""
from datetime import datetime
from datetime import timedelta
import random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import db.db as db

now = datetime.now()
end = now + timedelta(minutes=1)
current_time = now.strftime("%H:%M:%S")
end_time = end.strftime("%H:%M:%S")

sthlm_lat_one = 59.332936
sthlm_lat_two = 59.349901
sthlm_lng_one = 18.051605
sthlm_lng_two = 18.106993

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

gbg_lat_one = 57.684963
gbg_lat_two = 57.699499
gbg_lng_one = 11.931808
gbg_lng_two = 11.990259

def scooter_gbg(name):
    start_lat = random.uniform(gbg_lat_one, gbg_lat_two)
    start_lng = random.uniform(gbg_lng_one, gbg_lng_two)
    data = {
        "active_user": name,
        "city_location": "Göteborg",
        "lat": start_lat,
        "lng": start_lng,
        "start_time": current_time,
        "event": "Simulering för " + name,
        "start_lat": start_lat,
        "start_lng": start_lng,
        "end_time": end_time,
        "end_lat": random.uniform(gbg_lat_one, gbg_lat_two),
        "end_lng": random.uniform(gbg_lng_one, gbg_lng_two)
    }
    return data

malmo_lat_one = 55.567301
malmo_lat_two = 55.588695
malmo_lng_one = 12.925091
malmo_lng_two = 13.033399

def scooter_malmo(name):
    start_lat = random.uniform(malmo_lat_one, malmo_lat_two)
    start_lng = random.uniform(malmo_lng_one, malmo_lng_two)
    data = {
        "active_user": name,
        "city_location": "Malmö",
        "lat": start_lat,
        "lng": start_lng,
        "start_time": current_time,
        "event": "Simulering för " + name,
        "start_lat": start_lat,
        "start_lng": start_lng,
        "end_time": end_time,
        "end_lat": random.uniform(malmo_lat_one, malmo_lat_two),
        "end_lng": random.uniform(malmo_lng_one, malmo_lng_two),
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

def add_ten_sec(start_time):
    to_date_time = datetime.strptime(start_time, "%H:%M:%S")

    add_ten = to_date_time + timedelta(seconds=10)
    new_time = add_ten.strftime("%H:%M:%S")

    return new_time

def update_scooter_done(id, city, battery, lat, lng):
    point = Point(lat, lng)
    parkingzones = db.getParkingZones(city)

    for zone in parkingzones:
        polygon = Polygon([(zone.get('position').get('polygonePart1').get('lat'), zone.get('position').get('polygonePart1').get('lng')), (zone.get('position').get('polygonePart2').get('lat'), zone.get('position').get('polygonePart2').get('lng')), (zone.get('position').get('polygonePart3').get('lat'), zone.get('position').get('polygonePart3').get('lng')), (zone.get('position').get('polygonePart4').get('lat'), zone.get('position').get('polygonePart4').get('lng'))])

        if polygon.contains(point):
            data = {
                "city": city,
                "amount_of_bikes": zone.get('amount_of_bikes_zone') + 1,
                "color": zone.get('color')
            }
            print("Uppdaterade zonen: " + zone.get('color'))
            db.updateAmountOfBikesPark(data)

    data = {
        "_id": id,
        "battery": battery,
        "speed": 0,
        "lat": lat,
        "lng": lng
    }
    return data

""" DB conections """
import requests
import json
import os

try:
    with open("config.json", "r") as config:
        token_config = json.load(config)
except:
    print("Error")

url = 'localhost'
# print(type(os.environ['TOKEN']))
# print(os.environ['TOKEN'])
get_token = os.environ.get('TOKEN') or token_config

token = {
    "x-access-token": get_token
}

def get_scooters():
    """ Get scooters """
    result = requests.get('http://' + url + ':1337/api/scooter')
    res = result.json()
    return res.get('data')

def get_one_scooter(_id):
    """ Get one scooters """
    result = requests.get('http://' + url + ':1337/api/scooter/' + _id)
    return result.json()

def create_scooter(payload):
    """ Create scooters """
    print("I was here")
    result = requests.post('http://' + url + ':1337/api/scooter', data=payload, headers=token)
    res = result.json()
    print(res)
    res_data = res.get('data')
    print(res_data)
    return res_data

def update_scooter(payload):
    """ Update scooters """
    result = requests.put('http://' + url + ':1337/api/scooter', data=payload, headers=token)
    return result.text

def update_status(_id):
    """ Set user to null """
    result = requests.put('http://' + url + ':1337/api/scooter/setuser', data=_id, headers=token)
    return result.text

def delete_scooter(_id):
    """ Delete scooter """
    data = {
        "_id": _id
        }
    result = requests.delete('http://' + url + ':1337/api/scooter', data=data, headers=token)
    return result.text

def get_customers():
    """ Get customers """
    result = requests.get('http://' + url + ':1337/api/customers')
    res = result.json()
    return res.get('data')

def get_one_customer(_id):
    """ Get one customer """
    result = requests.get('http://' + url + ':1337/api/customers/' + _id)
    res = result.json()
    res_data = res.get('data')
    return res_data.get('username')

def create_customer(payload):
    """ Create customer """
    result = requests.post('http://' + url + ':1337/api/customers/register', data=payload, headers=token)
    res = result.json()
    res_data = res.get('data')
    return res_data.get('insertedId')

def delete_customer(_id):
    """ Delete customer """
    data = {
        "_id": _id
        }
    result = requests.delete('http://' + url + ':1337/api/customers', data=data, headers=token)
    return result.text

def get_parking_zones(city):
    """ Get parking zones """
    result = requests.get('http://' + url + ':1337/api/cities/zones/' + city)
    res = result.json()
    return res.get('data')

def update_amount_of_bikes_park(payload):
    """ Update amout of scooters in paring zone """
    result = requests.put('http://' + url + ':1337/api/cities/zones/update', data=payload, headers=token)
    return result.text

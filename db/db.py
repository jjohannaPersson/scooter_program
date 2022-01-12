""" DB conections """
import requests

def get_scooters():
    """ Get scooters """
    result = requests.get('http://localhost:1337/api/scooter')
    res = result.json()
    return res.get('data')

def get_one_scooter(_id):
    """ Get one scooters """
    result = requests.get('http://localhost:1337/api/scooter/' + _id)
    return result.json()

def create_scooter(payload):
    """ Create scooters """
    result = requests.post('http://localhost:1337/api/scooter', data=payload)
    res = result.json()
    res_data = res.get('data')
    return res_data
    # return res_data.get('insertedId')

def update_scooter(payload):
    """ Update scooters """
    result = requests.put('http://localhost:1337/api/scooter', data=payload)
    return result.text

def update_status(_id):
    """ Set user to null """
    result = requests.put('http://localhost:1337/api/scooter/setuser', data=_id)
    return result.text

def insert_logg(payload):
    """ InsertLogg to scooter """
    result = requests.put('http://localhost:1337/api/insertLogg', data=payload)
    return result.text

def delete_scooter(_id):
    """ Delete scooter """
    data = {
        "_id": _id
        }
    result = requests.delete('http://localhost:1337/api/scooter', data=data)
    return result.text

def get_customers():
    """ Get customers """
    result = requests.get('http://localhost:1337/api/customers')
    res = result.json()
    return res.get('data')

def get_one_customer(_id):
    """ Get one customer """
    result = requests.get('http://localhost:1337/api/customers/' + _id)
    res = result.json()
    res_data = res.get('data')
    return res_data.get('username')

def create_customer(payload):
    """ Create customer """
    result = requests.post('http://localhost:1337/api/customers/register', data=payload)
    res = result.json()
    res_data = res.get('data')
    return res_data.get('insertedId')

def delete_customer(_id):
    """ Delete customer """
    data = {
        "_id": _id
        }
    result = requests.delete('http://localhost:1337/api/customers', data=data)
    return result.text

def get_parking_zones(city):
    """ Get parking zones """
    result = requests.get('http://localhost:1337/api/cities/zones/' + city)
    res = result.json()
    return res.get('data')

def update_amount_of_bikes_park(payload):
    """ Update amout of scooters in paring zone """
    result = requests.put('http://localhost:1337/api/cities/zones/update', data=payload)
    return result.text

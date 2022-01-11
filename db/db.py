import requests

def getScooters():
    r = requests.get('http://localhost:1337/api/scooter')
    res = r.json()
    return res.get('data')

def getOneScooter(id):
    r = requests.get('http://localhost:1337/api/scooter/' + id)
    return r.json()

def createScooter(payload):
    r = requests.post('http://localhost:1337/api/scooter', data=payload)
    res = r.json()
    resData = res.get('data')
    return resData
    # return resData.get('insertedId')

def updateScooter(payload):
    r = requests.put('http://localhost:1337/api/scooter', data=payload)
    return r.text

def insertLogg(payload):
    r = requests.put('http://localhost:1337/api/insertLogg', data=payload)
    return r.text

def deleteScooter(id):
    data = {
        "_id": id
        }
    r = requests.delete('http://localhost:1337/api/scooter', data=data)
    return r.text

def getCustomers():
    r = requests.get('http://serlocalhostver:1337/api/customers')
    res = r.json()
    return res.get('data')

def getOneCustomer(id):
    r = requests.get('http://localhost:1337/api/customers/' + id)
    res = r.json()
    resData = res.get('data')
    return resData.get('username')

def createCustomer(payload):
    r = requests.post('http://localhost:1337/api/customers/register', data=payload)
    res = r.json()
    resData = res.get('data')
    return resData.get('insertedId')

def deleteCustomer(id):
    data = {
        "_id": id
        }
    r = requests.delete('http://localhost:1337/api/customers', data=data)
    return r.text

def getParkingZones(city):
    r = requests.get('http://localhost:1337/api/cities/zones/' + city)
    res = r.json()
    return res.get('data')

def updateAmountOfBikesPark(payload):
    r = requests.put('http://localhost:1337/api/cities/zones/update', data=payload)
    return r.text

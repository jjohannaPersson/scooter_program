import requests

# def getScooters():
#     r = requests.get('http://localhost:1337/api/scooter')
#     return r.json()

def getOneScooter(id):
    r = requests.get('http://localhost:1337/api/scooter/' + id)
    return r.json()

def createScooter(payload):
    r = requests.post('http://localhost:1337/api/scooter', data=payload)
    res = r.json()
    resData = res.get('data')
    return resData.get('insertedId')

def updateScooter(payload):
    r = requests.put('http://localhost:1337/api/scooter', data=payload)
    return r.text

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

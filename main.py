"""
Main program for simulating scooters
"""
from time import sleep
import db.db as db
import data.scooters
import data.customers

# scootersID = []
scooters = []
# customersID = []
customersNames= []

def delete_customers():
    """
    Clean up
    """
    allCustomers = db.getCustomers();

    for customer in allCustomers:
        name = customer.get('username')
        id = customer.get('_id')
        if name[0:4] == "Kund":
            db.deleteCustomer(id)
            print("Deleted: " + name)

def delete_scooters():
    """
    Clean up
    """
    allScooters = db.getScooters();

    for scooter in allScooters:
        name = scooter.get('active_user')
        id = scooter.get('_id')
        if name is None:
            continue
        elif name[0:4] == "Kund":
            db.deleteScooter(id)
            print("Deleted scooter: " + name)

def get_scooters():
    """
    Get all scooters
    """

    allScooters = db.getScooters();
    scooters.clear()

    for scooter in allScooters:
        name = scooter.get('active_user')
        if name is None:
            continue
        elif name[0:4] == "Kund":
            scooters.append(scooter)

    return scooters

def get_customers():
    """
    Get all customers
    """
    customersNames = []
    allCustomers = db.getCustomers();

    for customer in allCustomers:
        name = customer.get('username')
        if name[0:4] == "Kund":
            customersNames.append(name)

    return customersNames

def create_scooters():
    """
    Create scooters and pair with a customer
    """
    for i in range(1, len(customersNames)+1):
        if i <= 33:
            payload = data.scooters.scooter_sthlm(customersNames[i-1]);
            db.createScooter(payload)
            print("Done sthlm")
        elif i > 33 and i <= 66:
            payload = data.scooters.scooter_gbg(customersNames[i-1]);
            db.createScooter(payload)
            print("Done gbg")
        elif i > 66 and i <= 100:
            payload = data.scooters.scooter_malmo(customersNames[i-1]);
            db.createScooter(payload)
            print("Done malmö")

def create_customers(num):
    """
    Create customers
    """
    for i in range(1, int(num)+1):
        payload = data.customers.customer(i)
        customersID.append(db.createCustomer(payload))
        print("Kund nr: " + str(i))

    for customer in customersID:
        customersNames.append(db.getOneCustomer(customer))

def run_scooters():
    """
    Simulate scooters
    """
    start = scooters[0].get('start_time')
    end = scooters[0].get('logg')[0].get('end').get('time')
    print(start)
    print(end)

    while True:
        get_scooters();
        for scooter in scooters:
            payload = data.scooters.update_scooter(scooter.get('_id'), scooter.get('position').get('lat'), scooter.get('position').get('lng'), scooter.get('battery'), scooter.get('logg')[-1].get('end').get('position').get('lat'), scooter.get('logg')[-1].get('end').get('position').get('lng'))
            db.updateScooter(payload)

        current_time = data.scooters.add_ten_sec(start)
        start = current_time

        print("Tid just nu: " + start)
        if current_time[0:2] == end[0:2] and current_time[3:5] == end[3:5]:
            for scooter in scooters:
                payload = data.scooters.update_scooter_done(scooter.get('_id'), scooter.get('city_location'), scooter.get('battery'), scooter.get('logg')[-1].get('end').get('position').get('lat'), scooter.get('logg')[-1].get('end').get('position').get('lng'))
                db.updateScooter(payload)
            print("Thank you for this trip!")
            break;

def main():
    """
    Main
    """
    # amout_to_simulate = input("How many scooters do you want to simulate? ")
    #
    # print("Antal: " + amout_to_simulate)
    #
    # create_customers(amout_to_simulate)
    get_customers();
    create_scooters();
    get_scooters();
    run_scooters();

    # delete_customers()
    # delete_scooters()


if __name__ == "__main__":
    main()

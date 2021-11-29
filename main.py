"""
Main program for simulating scooters
"""
from time import sleep
import db.db as db
import data.scooters
import data.customers

scootersID = []
scooters = []
customersID = []
customersNames= []

def get_scooters():
    """
    Get all scooters
    """
    scooters.clear()
    for i in scootersID:
        scooters.append(db.getOneScooter(i))

    # print(scooters)
    return scooters

def create_scooters():
    """
    Create scooters and pair with a customer
    """
    for i in range(1, len(customersNames)+1):
        if i <= 25:
            payload = data.scooters.scooter_sthlm(customersNames[i-1]);
            scootersID.append(db.createScooter(payload))
            print("Done sthlm")
        elif i > 25 and i <= 50:
            payload = data.scooters.scooter_gbg(customersNames[i-1]);
            scootersID.append(db.createScooter(payload))
            print("Done gbg")
        elif i > 50 and i <= 75:
            payload = data.scooters.scooter_malmo(customersNames[i-1]);
            scootersID.append(db.createScooter(payload))
            print("Done malmö")
        elif i > 75 and i <= 75:
            payload = data.scooters.scooter_orebro(customersNames[i-1]);
            scootersID.append(db.createScooter(payload))
            print("Done örebro")

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
    Update position every 10th second
    """
    start = scooters[0].get('data')[0].get('start_time')
    end = scooters[0].get('data')[0].get('logg')[0].get('end').get('time')
    print(start)
    print(end)

    while True:
        get_scooters();
        # Uppdatera lat, lng, minska batteri med 1, sätt speed till 10
        for scooter in scooters:
            payload = data.scooters.update_scooter(scooter.get('data')[0].get('_id'), scooter.get('data')[0].get('battery'))
            db.updateScooter(payload)
            current_time = data.scooters.add_10_sec(start)

        start = current_time

        print("Tid just nu: " + current_time)
        if current_time[0:2] == end[0:2] and current_time[3:5] == end[3:5]:
            print("Thank you for this trip!")
            break;

        sleep(10)

def main():
    """
    Main
    """
    amout_to_simulate = input("How many scooters do you want to simulate? ")

    print("Antal: " + amout_to_simulate)

    create_customers(amout_to_simulate)
    create_scooters();
    get_scooters();
    run_scooters();


if __name__ == "__main__":
    main()

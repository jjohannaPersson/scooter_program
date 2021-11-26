"""
Main program for simulating scooters
"""
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
    for i in scootersID:
        scooters.append(db.getOneScooter(i))

    print(scooters)
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

def main():
    """
    Main
    """
    amout_to_simulate = input("How many scooters do you want to simulate? ")

    print("Antal: " + amout_to_simulate)

    create_customers(amout_to_simulate)
    create_scooters();
    get_scooters();


if __name__ == "__main__":
    main()

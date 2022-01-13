"""
Main program for simulating scooters
"""
import db.db as db
import data.scooters
import data.customers

scooters = []
# customers_ID = []
customers_names= []

def delete_customers():
    """
    Clean up
    """
    all_customers = db.get_customers()

    for customer in all_customers:
        name = customer.get('username')
        _id = customer.get('_id')
        if name[0:4] == "Kund":
            db.delete_customer(_id)
            print("Deleted: " + name)

def delete_scooters(delEvent):
    """
    Clean up
    """
    all_scooters = db.get_scooters()

    for scooter in all_scooters:
        event = scooter.get('logg')[0].get('event')
        _id = scooter.get('_id')
        print()
        if event is None:
            continue
        elif event[15:19] == delEvent:
            db.delete_scooter(_id)
            print("Deleted: " + event)

def get_scooters():
    """
    Get all scooters
    """

    all_cooters = db.get_scooters()
    scooters.clear()

    for scooter in all_cooters:
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
    customers_names.clear()
    all_customers = db.get_customers()

    for customer in all_customers:
        name = customer.get('username')
        if name[0:4] == "Kund":
            customers_names.append(name)

    return customers_names

def create_scooters():
    """
    Create scooters and pair with a customer
    """
    for i in range(1, len(customers_names)+1):
        if i <= 33:
            payload = data.scooters.scooter_sthlm(customers_names[i-1])
            db.create_scooter(payload)
            print("Done sthlm")
        elif 33 < i <= 66:
            payload = data.scooters.scooter_gbg(customers_names[i-1])
            db.create_scooter(payload)
            print("Done gbg")
        elif 66 < i <= 100:
            payload = data.scooters.scooter_malmo(customers_names[i-1])
            db.create_scooter(payload)
            print("Done malmö")

# def create_customers(num):
#     """
#     Create customers
#     """
#     for i in range(1, int(num)+1):
#         payload = data.customers.customer(i)
#         customers_ID.append(db.create_customer(payload))
#         print("Kund nr: " + str(i))
#
#     for customer in customers_ID:
#         customers_names.append(db.get_one_customer(customer))

def run_scooters():
    """
    Simulate scooters
    """
    start = scooters[0].get('start_time')
    end = scooters[0].get('logg')[0].get('end').get('time')
    print(start)
    print(end)

    while True:
        get_scooters()
        for scooter in scooters:
            payload = data.scooters.update_scooter(scooter.get('_id'), +
            scooter.get('position').get('lat'), +
            scooter.get('position').get('lng'), scooter.get('battery'), +
            scooter.get('logg')[-1].get('end').get('position').get('lat'), +
            scooter.get('logg')[-1].get('end').get('position').get('lng'))
            db.update_scooter(payload)

        current_time = data.scooters.add_ten_sec(start)
        start = current_time

        print("Tid just nu: " + start)
        if current_time[0:2] == end[0:2] and current_time[3:5] == end[3:5]:
            for scooter in scooters:
                payload = data.scooters.update_scooter_done(scooter.get('_id'), scooter.get('city_location'), +
                scooter.get('battery'), +
                scooter.get('logg')[-1].get('end').get('position').get('lat'), +
                scooter.get('logg')[-1].get('end').get('position').get('lng'))
                db.update_scooter(payload)
                db.update_status({"_id": scooter.get('_id')})
            print("Thank you for this trip!")
            break

def main():
    """
    Main
    """
    # create_customers(100)
    get_customers()
    create_scooters()
    get_scooters()
    run_scooters()

    # delete_customers()
    # delete_scooters("Kund")


if __name__ == "__main__":
    main()

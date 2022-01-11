"""
Data models for creating new cutsomers
"""

def customer(num):
    """ Create customers """
    data = {
        "username": "Kund" + str(num)
        }
    return data

import json
import os

CONTACT_FILE = "contacts.json"

def load_contacts():

    if not os.path.exists(CONTACT_FILE):

        with open(CONTACT_FILE, "w") as f:
            json.dump({}, f)

    with open(CONTACT_FILE, "r") as f:
        return json.load(f)

def save_contact(name, number):

    contacts = load_contacts()

    contacts[name.lower()] = number

    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

    return f"Saved contact {name}, Boss."

def get_contact(name):

    contacts = load_contacts()

    return contacts.get(name.lower())
"""A simple contact and address book manager."""

import csv
import hashlib
import json
import re

CONTACTS = {}
PHONE_PATTERN = re.compile(r"[0-9]{10}")


def add_contact(full_name, phone, email="", city="Unknown"):
    """Add a contact after validating the phone number."""
    if not PHONE_PATTERN.fullmatch(phone):
        print("Invalid phone number for", full_name)
        return False

    CONTACTS[full_name] = {"phone": phone, "email": email, "city": city}
    return True


def contact_id(full_name):
    """Return a short, deterministic identifier for a contact name."""
    return hashlib.sha256(full_name.encode("utf-8")).hexdigest()[:6]


def search_contacts(query):
    """Find contacts whose name or phone number contains the query."""
    matches = []
    normalized_query = query.casefold()

    for name, info in CONTACTS.items():
        if normalized_query in name.casefold() or query in info["phone"]:
            matches.append(name)

    return matches


def update_city(full_name, city):
    """Update a contact's city, returning False if the contact is absent."""
    if full_name not in CONTACTS:
        print("No contact named", full_name)
        return False

    CONTACTS[full_name]["city"] = city
    return True


def contacts_by_city():
    """Return contact names grouped by their city."""
    grouped = {}
    for name, info in CONTACTS.items():
        grouped.setdefault(info["city"], []).append(name)
    return grouped


def print_directory():
    """Print the address book in alphabetical order."""
    for index, name in enumerate(sorted(CONTACTS), start=1):
        print(index, name, CONTACTS[name]["phone"])


def export_csv(file_name="contacts.csv"):
    """Export all contacts to a CSV file."""
    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for name, info in CONTACTS.items():
            writer.writerow(
                [name, info["phone"], info["email"], info["city"]]
            )


def backup_book(file_name="contacts.json"):
    """Save the address book as JSON without executable deserialization."""
    with open(file_name, "w", encoding="utf-8") as backup_file:
        json.dump(CONTACTS, backup_file, indent=4)


def restore_book(file_name="contacts.json"):
    """Restore contacts from a JSON backup file."""
    with open(file_name, "r", encoding="utf-8") as backup_file:
        restored_contacts = json.load(backup_file)

    if not isinstance(restored_contacts, dict):
        raise ValueError("The backup file must contain a contact dictionary.")

    return restored_contacts


def main():
    """Run a short demonstration of the address book features."""
    add_contact("Neha Sharma", "9876543210", "neha@example.com", "Bengaluru")
    add_contact("Rahul Verma", "9123456780", "rahul@example.com", "Mysuru")
    add_contact("Test User", "12345")
    add_contact("Kavya Nair", "9988776655", city="Bengaluru")
    update_city("Rahul Verma", "Chennai")
    update_city("Nobody", "Delhi")
    print_directory()
    print("Search 'ra':", search_contacts("ra"))
    print("By city:", contacts_by_city())
    print("Id for Neha:", contact_id("Neha Sharma"))
    export_csv()
    backup_book()
    restored = restore_book()
    first_contact = sorted(restored)[0] if restored else "None"
    print("Contacts restored:", len(restored), "| first:", first_contact)
    print(
        "Restored contacts match the in-memory address book:",
        restored == CONTACTS,
    )


if __name__ == "__main__":
    main()

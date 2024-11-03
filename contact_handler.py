import address_book

import re
import datetime


contacts = None


def add_contact(*args):
    is_exist, name, phone_number = args_processing(*args)

    if is_exist:
        contacts.add_record(address_book.Record(name, phone_number))
        print(f"Contact {name} added")

    else:
        print(f"Contact {name} was not added, try again, please.")


def change_contact(*args):
    if contacts is None or len(contacts) == 0:
        print("Phonebook is empty")
    is_exist, name, phone_number, new_number = args_processing(*args)
    if phone_number is None:
        print("Incorrect phone number")
    elif new_number is None:
        print("Incorrect new phone number")
    elif contacts.find(name):
        record = contacts.find(name)
        record.edit_phone(phone_number, new_number)
        print(f"Contact {name} was updated by phone number {new_number}")
    else:
        print(f"Contact {name} not found")


def show_contact(*args):
    if contacts is None or len(contacts) == 0:
        print("Phonebook is empty")
        return
    if len(args) == 0:
        name = get_name()
    else:
        name = args[0]
    if contacts.find(name):
        print(f"{name}: {contacts.find(name)}")
    else:
        print(f"Contact {name} not found")


def show_all():
    for items in contacts:
        print(f'{contacts.find(items)}')


def add_birthday(*args):
    name, birthday = None, None
    if args is None:
        name = get_name()
        record = contacts.find(name)
        if record:
            record.add_birthday(birthday)
            print("Birthday was added")
        else:
            print(f"Contact {name} was not found")
    elif len(args) == 2:
        name, birthday = args[0].strip(), args[1].strip()
        record = contacts.find(name)
        if record:
            record.add_birthday(birthday)
            print("Birthday was added")
        else:
            print(f"Contact {name} was not found")
    elif len(args) == 1:
        name = args[0].strip()
        record = contacts.find(name)
        if record:
            record.add_birthday(birthday)
            print("Birthday was added")
        else:
            print(f"Contact {name} was not found")
    else:
        print("Incorrect input")

def add_phone(*args):
    name, phone = None, None
    if args is None:
        name = get_name()
        phone = get_phone_number()
        record = contacts.find(name)
        if record:
            record.add_phone(phone)
            print("Phone was added")
        else:
            print(f"Contact {name} was not found")
    elif len(args) == 2:
        name, phone = args[0].strip(), args[1].strip()
        phone = get_phone_number(phone)
        record = contacts.find(name)
        if record:
            record.add_phone(phone)
            print("Phone was added")
        else:
            print(f"Contact {name} was not found")
    elif len(args) == 1:
        name = args[0].strip()
        record = contacts.find(name)
        if record:
            record.add_phone(get_phone_number)
            print("Phone was added")
        else:
            print(f"Contact {name} was not found")
    else:
        print("Incorrect input")


def show_birthday(*args):
    if len(args) != 0:
        name = args[0].strip()
    else:
        name = get_name()
    record = contacts.find(name)
    if record:
        birthday = record.birthday
        if birthday:
            print(f"Contact`s {name} birthday is {birthday}")
        else:
            print(f"Contact`s {name} birthday is not defined")
    else:
        print(f"Contact {name} was not found")


def birthdays():
    birthdays = []
    for names in contacts:
        record = contacts.get(names)
        birthdays.append({"name": record.name, "birthday": record.birthday})
    result = get_upcoming_birthdays(birthdays)
    if result:
        print(result)
    else:
        print("Not found birthdays next week")


def args_processing(*args) -> list[bool, str, str]:
    info = args
    name, phone_number = "", ""
    if info is None or len(info) == 0:
        name = get_name()
        phone_number = get_phone_number(None)
    elif len(info) == 1:
        if re.match("[0-9]", info[0].strip()):
            print(f"Incorrect contact name {info[0]}, contact wasn`t added")
            return False, None, None
        else:
            phone_number = get_phone_number(None)
            name = info[0].strip()
    else:
        if re.match("[0-9]", info[-1].strip()):
            phone_number = info[-1].strip()
            name = ""
            for item in info:
                if item != phone_number:
                    name += item + " "
            phone_number = get_phone_number(phone_number)
        else:
            print(f"Incorrect contact data {info}, contact wasn`t added")
            return False, None, None
    return name and phone_number, name, phone_number


def get_name() -> str:
    while True:
        name = input("Enter contact`s name:  ")
        if name:
            return name.strip()


def get_phone_number(number: str) -> str:
    while True:
        if number is None:
            number = input("Enter phone number: ")
        if number is not None:
            number = re.sub("[^0-9]", "", number.strip())

            # Suffix correction
            if len(number) == 12:
                return "+" + number
            if len(number) == 11:
                return "+3" + number
            if len(number) == 10:
                return "+38" + number
            return None


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:

    current_date = datetime.date.today()

    # Inputed date processing with validation
    result_list = []
    for i, user in enumerate(users):
        birthday = user["birthday"].value
        if not birthday:
            continue
        # Calculate birthday in the current year
        birthday_current_year = birthday.replace(year=current_date.year)

        # Check if birthday has already passed in the current year
        if birthday_current_year < current_date:
            birthday_current_year = birthday.replace(year=current_date.year + 1)

        # Calculate appropriate congratulation date (considering weekends)
        congratulation_date = birthday_current_year
        if birthday_current_year.weekday() == 5:
            congratulation_date += datetime.timedelta(days=2)
        elif birthday_current_year.weekday() == 6:
            congratulation_date += datetime.timedelta(days=1)

        # Calculate the number of days until the congratulation date
        days_until_congratulation = (congratulation_date - current_date).days

        # Add user information to the result list if birthday is within the week
        if 0 <= days_until_congratulation <= 7:
            user_congrat = {
                "name": user["name"].value,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                "birthday_date": birthday.strftime("%Y.%m.%d"),
            }
            result_list.append(user_congrat)

    return result_list

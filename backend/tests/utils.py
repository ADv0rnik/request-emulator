import random
import string

import names


def generate_book_id() -> int:
    list_of_ids = [1, 2]
    return random.choice(list_of_ids)


def generate_name() -> str:
    gender_choice = ['female', 'male']
    return names.get_first_name(gender=random.choice(gender_choice))


def construct_email() -> str:
    full_name = names.get_first_name() + names.get_last_name()
    return "".join(full_name.lower()) + "@yahoo.com"


def generate_password() -> str:
    return "".join(
        random.choices(string.ascii_lowercase, k=6)
        + random.choices(string.ascii_uppercase, k=2)
        + random.choices(string.digits)
        + random.choices("!@&*%?$")
    )

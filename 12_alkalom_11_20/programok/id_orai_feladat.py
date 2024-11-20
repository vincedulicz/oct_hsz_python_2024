import json
import random
import string
from datetime import datetime, timedelta


names = ["John Doe",
         "Jane Smith",
         "Alice Johnson",
         "Bob Brown",
         "Charlie Davis",
         "Emily Clark"
         ]


def generate_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def generate_born_date():
    year = random.randint(1920, 1980)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # egyszerűsítve
    return f"{year:04d}.{month:02d}.{day:02d}"


def generate_age(born_date):
    birth_year = int(born_date.split('.')[0])
    current_year = datetime.now().year
    return current_year - birth_year


def generate_country():
    return random.choice(["HU", "EU", "USA", "SP"])


def generate_worker():
    return random.choice([True, False])


def generate_valid_until():
    return datetime.now() + timedelta(days=random.randint(0, 365))


def generate_random_json(num_users=10):
    users = {}
    for _ in range(num_users):
        user_id = f"user-{generate_user_id()}"
        born_date = generate_born_date()
        age = generate_age(born_date)

        users[user_id] = {
            "valid_until": generate_valid_until().strftime("%Y.%m.%d"),
            "born-date": born_date,
            "name": random.choice(names),
            "age": age,
            "country": generate_country(),
            "worker": generate_worker(),
            "other": []
        }
    return users


def save_json_to_txt(file_name, num_users=10):
    random_json = generate_random_json(num_users)
    with open(file_name, 'w') as file:
        json.dump(random_json, file, indent=4)


def read_json_from_txt(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


def check_and_save_expiring_users(input_file, output_file):
    data = read_json_from_txt(input_file)
    expiring_users = {}

    for user_id, user_info in data.items():
        valid_until = datetime.strptime(user_info['valid_until'], "%Y.%m.%d")
        days_left = (valid_until - datetime.now()).days

        if days_left <= 180:
            expiring_users[user_id] = user_info

    if expiring_users:
        with open(output_file, 'w') as file:
            json.dump(expiring_users, file, indent=4)


def save_no_worker_users(input_file, output_file):
    data = read_json_from_txt(input_file)
    no_worker_users = {user_id: user_info for user_id, user_info in data.items()
                       if not user_info['worker']}

    if no_worker_users:
        with open(output_file, 'w') as file:
            json.dump(no_worker_users, file, indent=4)


def save_over_65_users(input_file, output_file):
    data = read_json_from_txt(input_file)
    over_65_users = {user_id: user_info for user_id, user_info in data.items()
                     if user_info['age'] > 65}

    if over_65_users:
        with open(output_file, 'w') as file:
            json.dump(over_65_users, file, indent=4)


def save_middle_eu_users(input_file, output_file):
    data = read_json_from_txt(input_file)
    middle_eu_users = {user_id: user_info for user_id, user_info in data.items()
                       if user_info['country'] == 'HU'}

    if middle_eu_users:
        with open(output_file, 'w') as file:
            json.dump(middle_eu_users, file, indent=4)


def main():
    save_json_to_txt("adatok/random_user_data.txt")

    check_and_save_expiring_users("adatok/random_user_data.txt", "adatok/expire180.json")

    save_no_worker_users("adatok/random_user_data.txt", "adatok/no_worker.json")

    save_over_65_users("adatok/random_user_data.txt", "adatok/over65.json")

    save_middle_eu_users("adatok/random_user_data.txt", "adatok/middle_eu.json")


if __name__ == "__main__":
    main()

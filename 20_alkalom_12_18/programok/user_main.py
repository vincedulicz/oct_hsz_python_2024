from o_20_alkalom_12_18.backend.feladat_usergenerator.filemanager.FileManager import FileManager
from o_20_alkalom_12_18.backend.feladat_usergenerator.user_generator.UserGenerator import UserGenerator
from o_20_alkalom_12_18.backend.feladat_usergenerator.userprocessor.UserProcessor import UserProcessor


def main():
    names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis", "Emily Clark"]

    user_generator = UserGenerator(names)
    file_manager = FileManager()
    user_processor = UserProcessor()

    num_user = 10
    users = {}

    for _ in range(num_user):
        users.update(user_generator.random_user())

        file_manager.save_to_file("data/random_user.txt", users)

        data = file_manager.read_from_file("data/random_user.txt")

        exp_users = user_processor.filter_expiring_users(data)
        file_manager.save_to_file("data/expire180.json", exp_users)

        over_65_users = user_processor.filter_over_age(data, 65)
        file_manager.save_to_file("data/over65.json", over_65_users)

main()
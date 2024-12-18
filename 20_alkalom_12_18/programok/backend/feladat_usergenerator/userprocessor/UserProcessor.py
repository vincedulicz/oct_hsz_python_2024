from datetime import datetime


class UserProcessor:
    """
    TODO: data mentése, így paraméteresen nem kell újra és újra átadni
    """

    DATA = None

    @classmethod
    def test_class(cls):
        return cls.DATA

    @staticmethod
    def filter_expiring_users(data, days=180):
        expiring_users = {}
        for user_id, user_info in data.items():
            valid_until = datetime.strptime(user_info['valid_until'], "%Y.%m.%d")
            if (valid_until - datetime.now()).days <= days:
                expiring_users[user_id] = user_info
        return expiring_users

    @staticmethod
    def filter_no_workers(data):
        return {user_id: user_info for user_id, user_info in data.items() if not user_info['worker']}

    @staticmethod
    def filter_over_age(data, age_limit):
        return {user_id: user_info for user_id, user_info in data.items() if user_info['age'] > age_limit}

    @staticmethod
    def filter_by_country(data, country):
        return {user_id: user_info for user_id, user_info in data.items() if user_info['country'] == country}



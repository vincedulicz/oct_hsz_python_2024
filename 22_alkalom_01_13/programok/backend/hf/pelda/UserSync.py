import requests


class UserSync:
    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def create_user(self, user_data) -> dict:
        url = f"{self.base_url}/post"
        response = requests.post(url, json=user_data)
        response.raise_for_status()

        return response.json()

    def get_user(self, user_id) -> dict:
        url = f"{self.base_url}/get"
        response = requests.get(url, params={"user_id": user_id})
        response.raise_for_status()

        return response.json()

    def update_user(self, user_id, update_data) -> dict:
        url = f"{self.base_url}/put"
        response = requests.put(url, json={"user_id": user_id, **update_data})
        response.raise_for_status()

        return response.json()

    def delete_user(self, user_id) -> dict:
        url = f"{self.base_url}/delete"
        response = requests.delete(url, params={"user_id": user_id})
        response.raise_for_status()

        return response.json()


if __name__ == "__main__":
    base_url = "https://httpbin.org"
    user_sync = UserSync(base_url)

    new_user = {"name": "John Doe", "email": "john.doe@example.com"}
    print("Új felhasználó létrehozása:", user_sync.create_user(new_user))

    print("Felhasználó lekérése:", user_sync.get_user(user_id=1))

    updated_data = {"name": "John Smith"}
    print("Felhasználó frissítése:", user_sync.update_user(user_id=1, update_data=updated_data))

    print("Felhasználó törlése:", user_sync.delete_user(user_id=1))

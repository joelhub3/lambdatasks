import logging
from typing import Optional, TypedDict

import requests


class AddUserInput(TypedDict):
    name: str
    email: str
    external_id: str
    password: str
    payment_id: str


class AddUserOutput(TypedDict):
    user_id: str
    username: str


class Backend:
    def __init__(self):
        # gets credentials and stuff
        self.base_url = "https://localhost:9000"
        self.auth = None

    def _get_auth(self):
        if self.auth is None:
            self.auth = "password123"
        return self.auth

    def add_user(self, user_data: AddUserInput) -> tuple[bool, Optional[AddUserOutput]]:
        """
        add_user creates a user on the backend. if successful, returns a 200 plus user information.
        Otherwise returns an error we don't care about
        """
        try:
            resp = requests.post(
                self.base_url + "/add-user",
                json=user_data,
                headers={
                    "Authorization": self._get_auth()
                }
            )
            if resp.status_code == 200:
                return True, resp.json()
        except Exception as e:
            logging.error(f"Unable to add user: {e}")
        return False, None

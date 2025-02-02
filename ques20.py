from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self, username, password):
        print(f"Logging in to Google with username: {username}")

    def logout(self):
        print("Logging out from Google")

class FacebookAuth(UserAuthentication):
    def login(self, username, password):
        print(f"Logging in to Facebook with username: {username}")

    def logout(self):
        print("Logging out from Facebook")

google_auth = GoogleAuth()
facebook_auth = FacebookAuth()

google_auth.login("user@example.com", "password123")
google_auth.logout()

facebook_auth.login("user@example.com", "password123")
facebook_auth.logout()

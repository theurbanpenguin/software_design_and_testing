class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class UserDatabase:
    def save(self, user: User):
        print(f"User {user.name} saved to database.")


user = User("bob", "bob@gmail.com")
UserDatabase().save(user)

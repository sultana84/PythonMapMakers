MOCK_USERS = [{"email": "test@gmail.com", "salt": "e10adc3949ba59abbe56e057f20f883e=", "hashed": "123456"}]

class dbhelp:

    def get_user(self,email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[email]
        return None

    def add_user(self, email, salt, hashed):
     MOCK_USERS.append({"email": email, "salt": salt, "hashed": hashed})


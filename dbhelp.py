MOCK_USERS = {'test@gmail.com': '654321'}

class dbhelp:

    def get_user(self,email):
        if email in MOCK_USERS:
            return MOCK_USERS[email]
        return None


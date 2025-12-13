class Admin:
    def create_user(self, username):
        print(f"Пользователь {username} создан")

class Support:
    def create_ticket(self, issue):
        print(f"Тикет {issue} создан")

class SuperUser(Admin, Support):
    pass

su = SuperUser()
su.create_user("Vlad")
su.create_ticket("Течет крыша")
def require_role(role):
    def decorator(func):
        def wrapper(user):
            if user == role:
                print(func())
            else:
                print(f"Ошибка: Требуется роль {role}, текущая роль: {user}")
        return wrapper
    return decorator


@require_role("admin")
def admin_test():
    print("Выполняется админский тест")
    return "Success"

user_one = "user"
user_two = "admin"

admin_test(user_one)
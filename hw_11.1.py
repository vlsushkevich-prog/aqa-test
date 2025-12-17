def test_info(author, component):
    def decorator(cls):
        cls.author = author
        cls.component = component
        return cls
    return decorator

@test_info("Vlad", "Auth")
class TestLogin:
    pass

print(TestLogin.author)
print(TestLogin.component)
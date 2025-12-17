PAGES = []

def register_page(cls):
    PAGES.append(cls)
    return cls

@register_page
class LoginPage:
    pass

@register_page
class DashboardPage:
    pass

print([cls.__name__ for cls in PAGES])
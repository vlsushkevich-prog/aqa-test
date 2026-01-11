def create_settings_dict(src):
    with open(src, 'r', encoding='utf-8') as f:
        settings_dict = {}
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=')
                settings_dict[key] = value
        print(settings_dict)

create_settings_dict('config.txt')



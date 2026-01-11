def log_message(path, message):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

log_message('app.log', 'Test failed')
log_message('app.log', 'Test passed')
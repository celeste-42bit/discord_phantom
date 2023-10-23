import os, time

def log(message):
    # Get the size of the log file in bytes
    size = os.path.getsize('./logs/message.log')

    # If the log file exceeds 10MB, delete it and create a new one
    if size >= 10000000000:  # size in bytes (100M sounds good?)
        print('The log file was bigger then 10MB and has been deleted')
        os.remove('./logs/message.log')
        create()
    # Write the message to the log file
    with open('./logs/message.log', '+a', encoding='utf-8') as log:
        log.write(f'{message}\n')

def create():
    print('A new log file has been created')
    with open('./logs/message.log', '+w', encoding='utf-8') as log:  # If writable file doesn't exist, create first, then write...
        log.write(f'This log was created at {time.gmtime()}\n')

if not os.path.exists('./logs/message.log'):
    create()
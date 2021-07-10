def new_func():
    Mail = input('Please enter the mail ID: ')
    try:
        i = Mail.index('@')
        print('Mail ID contian @ symbol, which is mandatory')
    except ValueError:
        print('Mail ID does not contain the @ symbol, which is mandatory')

new_func()  

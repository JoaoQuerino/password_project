from hash_generator import gerar_hashs
from password_generator import generate_password


print('*** Select a function to use ***')
print('*** 1 - password generator ***')
print('*** 2 - Hash generator ***')

selected_function = input('Function selected: ')
while True:
    if selected_function == '1':
        try:
            password_final = generate_password()
            print(password_final)
        except Exception as e:
            print(e)
    if selected_function == '2':
        try:
            password = input('Inform the password: ')
            generated_hashs = gerar_hashs(password)
            for h in generated_hashs:
                print('\n')
                print(h)
        except Exception as e:
            print(e)

    exit_while = input('Do you want to leave the function? type Y to exit\n')
    if exit_while.lower() == 'y':
        break

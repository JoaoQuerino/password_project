from hash_generator import create_has
from password_generator import generate_password
from common import get_user_input_generic
from my_interface import form_check_password, form_main


# TODO Finalizar formulario do password generator
while True:
    form_main(1, 2, 3, 4)
    print('*** Select a function to use ***')
    print('*** 1 - password generator ***')
    print('*** 2 - Hash generator ***')
    print('*** 3 - Hash generator by password ***')
    print('*** 4 - Check password ***')

    selected_function = get_user_input_generic('Function selected: ', 'Error processing function input')
    if selected_function == 1:
        try:
            password_final = generate_password()
            print(f'The password generated is: {password_final}')
        except Exception as e:
            print(e)
    elif selected_function == 2:
        try:
            password = input('Inform the password: ')
            generated_has = create_has(password)
            for h in generated_has:
                print('\n')
                print(h)
        except Exception as e:
            print(e)
    elif selected_function == 3:
        try:
            if password_final:
                generated_has = create_has(password_final)
                for h in generated_has:
                    print('\n' + h)
            else:
                print('No password found')
        except Exception as e:
            print(e)

    elif selected_function == 4:
        try:
            form_check_password()
        except Exception as e:
            print(e)
    else:
        print('Invalid function')

    exit_while = input('\nDo you want to leave the function? type Y to exit\n')
    if exit_while.lower() == 'y':
        break

from hash_generator import create_has, create_has_sha1
from password_generator import generate_password
from common import get_user_input_generic


while True:
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
            check_password = get_user_input_generic('Inform the password to create a hash: ', 'Invalid error', str)
            has_by_password = create_has_sha1(check_password)
            print(has_by_password)
            string_to_compare = get_user_input_generic('Inform the string to compare with the hash', 'Input error', str)
            string_to_compare = create_has_sha1(string_to_compare)
            if string_to_compare == has_by_password:
                print('The password is right')
            else:
                print('The second password is different')

        except Exception as e:
            print(e)

    else:
        print('Invalid function')

    exit_while = input('\nDo you want to leave the function? type Y to exit\n')
    if exit_while.lower() == 'y':
        break

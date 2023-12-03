import random
import string


def select_type() -> list:
    valid = False
    char = ''
    while not valid:
        print('Select the type of password')
        print('1 - numbers')
        print('2 - special characters')
        print('3 - any characters')
        print('4 - letters')
        type_selected = input('Inform the type: ')

        if type_selected in ['1', '2', '3', '4']:
            if type_selected == '1':
                char = string.digits
                valid = True

            elif type_selected == '2':
                char = string.punctuation
                valid = True

            elif type_selected == '3':
                char = string.printable
                valid = True

            elif type_selected == '4':
                char = string.ascii_letters
                valid = True
            else:
                print('Type of character Error')

    char = list(char)
    return char


def generate_password():
    characters_type_selected = select_type()
    while True:
        try:
            num_char = int(input('Inform the number of characters: '))
            if num_char != '':
                password_generated = random.choices(characters_type_selected, k=num_char)
                password_generated_in_string = ''.join(password_generated)
                return password_generated_in_string
            elif num_char < 1:
                print('Invalid number')
        except ValueError:
            print('Invalid value')


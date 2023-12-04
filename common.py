def get_user_input_generic(prompt, error_message, data_type=int):
    """
    Get user input with error handling for the specified data type.

    Args:
        prompt (str): The prompt to display to the user.
        error_message (str): The error message to display on invalid input.
        data_type (type, optional): The data type to convert the user input.
            Default is int.

    Returns:
        Any: User input of the specified data type.
    """
    while True:
        try:
            user_input = data_type(input(prompt))
            break
        except ValueError:
            print(error_message)
    return user_input
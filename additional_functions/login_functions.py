def login_ok(dictionary):
    """
    web request -> ?login=login_name&password=passwd
    :param dictionary: {'login': 'login_name', 'password': 'passwd'}
    :return:
    """
    if not isinstance(dictionary, dict):
        return False
    if not 'login' in dictionary or not 'password' in dictionary:
        return False

    if dictionary['login'] == 'login_name' and dictionary['password'] == 'passwd':
        return True

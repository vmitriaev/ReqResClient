def error_constructor(message):
    '''Вывод сообщения об ошибке'''
    errorMessage = ('ERROR: ' + message)
    lines = '-' * len(errorMessage)
    return '\n' + lines + '\n' + errorMessage + '\n' + lines + '\n'


def counter(count):
    '''Запоминает количество'''
    return count


def low_maker(text):
    lower_text = str(text).lower()
    return lower_text


def service_switcher(service_value):
    return {
        '1': 'users',
        '2': 'unknown',
        '3': 'register',
        '4': 'login'
    }.get(service_value, error_constructor(choose_error + service_value.upper()))


def method_switcher(method_value):
    return {
        '1': 'get',
        '2': 'post',
        '3': 'put',
        '4': 'patch',
        '5': 'delete'
    }.get(method_value, error_constructor(choose_error + method_value.upper()))


def users_get_param_switcher(users_get_param_value):
    return {
        '1': 'user_list',
        '2': 'single_user',
        '3': 'delayed_response'
    }.get(users_get_param_value, error_constructor(choose_error + users_get_param_value.upper()))


def unknown_get_param_switcher(unknown_get_param_value):
    return {
        '1': 'resource_list',
        '2': 'resource_single'
    }.get(unknown_get_param_value, error_constructor(choose_error + unknown_get_param_value.upper()))

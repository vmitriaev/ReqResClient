import json
from errors import error


def Res(data):
    '''Вывод ответа'''
    j = json.dumps(data.json(), sort_keys=True, indent=2)
    c = data.status_code
    m = ('\nCode: ' + str(c) + '\n' + 'Response:' + '\n' + j + '\n')
    if c == 200:
        return '\nStatus: OK' + m

    elif c == 201:
        return '\nStatus: CREATED' + m

    elif c == 400:
        return '\nStatus: BAD REQUEST' + m

    elif c == 404:
        return '\nStatus: NOT FOUND' + m

    else:
        return error('unknown status code ' + str(c))

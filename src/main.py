from src.req import Req
from src.errors import error

while True:
    m = input('Type method (GET, POST, PUT, PATCH, DELETE), or STOP for exit: ')
    if m.lower() in ('get', 'delete'):
        u = input('Endpoint: https://reqres.in/api/')
        r = Req(m, u)
        print(r.send())

    elif m.lower() in ('post', 'put', 'patch'):
        u = input('Endpoint: https://reqres.in/api/')
        b = input('Body (JSON):\n')
        r = Req(m, u, b)
        print(r.send())

    elif m.lower() in ('exit', 'stop', '0'):
        break

    else:
        print(error('unknown method ' + m.upper()))

import json
from src.req import Req
from src.errors import error

with open("config.json") as config_file:
    conf = json.load(config_file)

stoplist = conf['stop_words']

while True:
    u = input(conf['endpoint_list']['basic_url'] + '/')
    m = input('Type method (GET, POST, PUT, PATCH, DELETE), or STOP for exit: ')
    if m.lower() in ('get', 'delete'):
        r = Req(m, u)
        print(r.send())

    elif m.lower() in ('post', 'put', 'patch'):
        b = input('Body (JSON):' + '\n' + '''''')
        r = Req(m, u, b)
        print(r.send())

    elif m.lower() in stoplist:
        break

    else:
        print(error('unknown method ' + m.upper()))

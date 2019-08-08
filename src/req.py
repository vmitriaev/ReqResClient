import requests, json
from src.errors import error
from src.res import res

with open("config.json") as config_file:
    conf = json.load(config_file)


class Req():
    '''Экземпляром класса является объект, имеющий атрибуты для отправки запроса: method, url, json'''

    def __init__(self, meth, url, body=None):
        '''Инициализация объекта класса Req'''
        self.meth = meth
        self.url = url
        self.body = body
        self.d_url = conf['endpoint_list']['basic_url'] + '/'

    def send(self):
        '''Отправка запроса'''
        s_meth = str(self.meth).lower()
        s_url = str(self.url).lower()
        f_url = str(self.d_url + s_url).lower()
        s_body = str(self.body).lower()

        if s_meth == 'get':
            i = requests.get(url=f_url)
            return res(i)

        elif s_meth == 'post':
            i = requests.post(url=f_url, data=s_body)
            return res(i)

        elif s_meth == 'put':
            i = requests.put(url=f_url, data=s_body)
            return res(i)

        elif s_meth == 'patch':
            i = requests.patch(url=f_url, data=s_body)
            return res(i)

        elif s_meth == 'delete':
            i = requests.delete(url=f_url)
            c = i.status_code
            if c == 204:
                return '\nStatus: NO CONTENT' + '\nCode: ' + str(c) + '\n'

            else:
                return error('unknown status code ' + str(c))

        else:
            return error('unknown method ' + s_meth.upper())

def error(message):
    '''Вывод сообщения об ошибке'''
    errMsg = ('ERROR: ' + message)
    lines = '-' * len(errMsg)
    return '\n' + lines + '\n' + errMsg + '\n' + lines + '\n'

import os


_commands = {}

def register(func):
    _commands[func.__name__] = func
    return func


def run_cmd(source, filename, symbol):
    print(source, filename, symbol)
    cmd, _, args = source.partition(' ')
    if cmd in _commands:
        func = _commands[cmd]
        print('args', args)
        return func(*args.split())
    return None


@register
def helpall(*args, **kwargs):
    return [cmd for cmd in _commands if cmd != 'helpall']

@register
def ls(*args, **kwargs):
    print('ls args', args)
    if not any(args):
        return os.listdir('.')
    contents = []
    for dir_ in args:
        try:
            content = os.listdir(dir_)
        except NotADirectoryError as err:
            contents.append(dir_)
        except FileNotFoundError as err:
            contents.append([''])
        else:
            contents.append(content)
    return contents



print(f'[a] Starting a, {__name__=}')
print('[a] About to import b')
import b
print('[a] Done importing b')

x = 'hello from a'

def hello(name):
    return 'Hello from a, {name}!'

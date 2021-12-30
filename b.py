print('[a] About to import b')
import b
print('[a] Done importing b')


print('[a] Starting a, {__name__=}')

x = 'hello from b'

def hello(name):
    return 'Hello from a, {name}!'

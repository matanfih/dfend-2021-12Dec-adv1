print(f'[b] Starting b, {__name__=}')
print('[b] About to import a')
import a
print('[b] Done importing a')

x = 'hello from b'

def hello(name):
    return 'Hello from b, {name}!'

print(f'[b] Starting b, {__name__=}')
print('[b] About to import a')
import a
print('[b] Done importing a')

print('[a] Starting a, {__name__=}')

x = 'hello from b'

def hello(name):
    return 'Hello from a, {name}!'

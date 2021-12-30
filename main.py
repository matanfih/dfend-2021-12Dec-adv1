print(globals())

print(f'[main] Starting main, {__name__=}')
print('[main] About to import a')
import a
print('[main] Done importing a')

print(globals())


print('[main] About to import b')
import b
print('[main] Done importing b')

print(globals())

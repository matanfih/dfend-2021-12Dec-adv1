def menu(*args):
    while True:
        s = input('Enter choice: ').strip()

        if s in args:
            return s

        print('Bad choice; try again')
        
    

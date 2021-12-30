def menu(*args):
    options = '/'.join(args)
    while True:
        s = input(f'Choose from {options}: ').strip()

        if s in args:
            return s

        print('Bad choice; try again')
        
    

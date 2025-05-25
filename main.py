import socket

if socket.gethostname() == 'lugia': # laptop
    import lugia.configuration
elif socket.gethostname() == 'magikarp': # desktop
    # TODO:
    pass
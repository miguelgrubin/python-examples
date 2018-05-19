import os
reldir = os.path.join(os.path.dirname(__file__), '..', '..')
print(reldir)
print(os.path.abspath(reldir))
print(os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'aemet')))

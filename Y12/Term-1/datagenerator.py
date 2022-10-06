from random import randint
def create_char():
    return chr(randint(48, 126))

mychar = create_char()
print(mychar)
